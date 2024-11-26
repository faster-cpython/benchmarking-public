# Results vs. base

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: darwin-arm64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.009x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                                | 176 ms: 1.02x faster                                                      |
| docutils       | 1.60 sec                                                              | 1.56 sec: 1.02x faster                                                    |
| html5lib       | 33.0 ms                                                               | 32.6 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager    | 65.9 ms                                                               | 64.7 ms: 1.02x faster                                                     |
| async_generators    | 297 ms                                                                | 294 ms: 1.01x faster                                                      |
| async_tree_eager_tg | 42.8 ms                                                               | 42.3 ms: 1.01x faster                                                     |
| async_tree_io       | 594 ms                                                                | 592 ms: 1.00x faster                                                      |
| coroutines          | 16.0 ms                                                               | 16.0 ms: 1.00x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (16): async_tree_none, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io_tg, async_tree_memoization, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization_tg, asyncio_tcp_ssl, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 288 ms                                                                | 282 ms: 1.02x faster                                                      |
| nbody          | 63.5 ms                                                               | 63.3 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 16.9 ms                                                               | 16.5 ms: 1.02x faster                                                     |
| regex_compile  | 75.7 ms                                                               | 73.9 ms: 1.02x faster                                                     |
| regex_dna      | 148 ms                                                                | 145 ms: 1.02x faster                                                      |
| regex_effbot   | 2.48 ms                                                               | 2.46 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_list          | 3.01 us                                                               | 2.94 us: 1.02x faster                                                     |
| pickle               | 7.44 us                                                               | 7.37 us: 1.01x faster                                                     |
| unpickle             | 9.35 us                                                               | 9.25 us: 1.01x faster                                                     |
| pickle_pure_python   | 179 us                                                                | 177 us: 1.01x faster                                                      |
| tomli_loads          | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                                    |
| xml_etree_process    | 34.8 ms                                                               | 34.8 ms: 1.00x slower                                                     |
| unpickle_pure_python | 131 us                                                                | 132 us: 1.00x slower                                                      |
| xml_etree_generate   | 51.0 ms                                                               | 51.2 ms: 1.00x slower                                                     |
| json_dumps           | 6.32 ms                                                               | 6.36 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (5): xml_etree_parse, unpickle_list, json_loads, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                               | 16.4 ms: 1.08x faster                                                     |
| genshi_xml      | 42.0 ms                                                               | 40.4 ms: 1.04x faster                                                     |
| django_template | 23.2 ms                                                               | 22.6 ms: 1.03x faster                                                     |
| Geometric mean  | (ref)                                                                 | 1.04x faster                                                              |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240910-darwin-arm64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                      | 1.56 sec                                                              | 1.45 sec: 1.08x faster                                                    |
| genshi_text              | 17.7 ms                                                               | 16.4 ms: 1.08x faster                                                     |
| scimark_lu               | 68.0 ms                                                               | 65.2 ms: 1.04x faster                                                     |
| genshi_xml               | 42.0 ms                                                               | 40.4 ms: 1.04x faster                                                     |
| pycparser                | 702 ms                                                                | 677 ms: 1.04x faster                                                      |
| fannkuch                 | 277 ms                                                                | 267 ms: 1.04x faster                                                      |
| sqlglot_optimize         | 36.7 ms                                                               | 35.5 ms: 1.03x faster                                                     |
| richards                 | 46.4 ms                                                               | 45.0 ms: 1.03x faster                                                     |
| richards_super           | 48.2 ms                                                               | 46.8 ms: 1.03x faster                                                     |
| logging_simple           | 3.09 us                                                               | 3.01 us: 1.03x faster                                                     |
| sqlglot_normalize        | 188 ms                                                                | 183 ms: 1.03x faster                                                      |
| go                       | 103 ms                                                                | 101 ms: 1.03x faster                                                      |
| django_template          | 23.2 ms                                                               | 22.6 ms: 1.03x faster                                                     |
| logging_format           | 3.39 us                                                               | 3.30 us: 1.03x faster                                                     |
| regex_v8                 | 16.9 ms                                                               | 16.5 ms: 1.02x faster                                                     |
| regex_compile            | 75.7 ms                                                               | 73.9 ms: 1.02x faster                                                     |
| pickle_list              | 3.01 us                                                               | 2.94 us: 1.02x faster                                                     |
| docutils                 | 1.60 sec                                                              | 1.56 sec: 1.02x faster                                                    |
| pidigits                 | 288 ms                                                                | 282 ms: 1.02x faster                                                      |
| async_tree_eager         | 65.9 ms                                                               | 64.7 ms: 1.02x faster                                                     |
| regex_dna                | 148 ms                                                                | 145 ms: 1.02x faster                                                      |
| sympy_str                | 146 ms                                                                | 144 ms: 1.02x faster                                                      |
| deepcopy_memo            | 16.4 us                                                               | 16.2 us: 1.02x faster                                                     |
| 2to3                     | 179 ms                                                                | 176 ms: 1.02x faster                                                      |
| meteor_contest           | 75.7 ms                                                               | 74.6 ms: 1.01x faster                                                     |
| sqlglot_transpile        | 1.06 ms                                                               | 1.04 ms: 1.01x faster                                                     |
| deepcopy_reduce          | 1.53 us                                                               | 1.51 us: 1.01x faster                                                     |
| hexiom                   | 4.77 ms                                                               | 4.71 ms: 1.01x faster                                                     |
| telco                    | 4.82 ms                                                               | 4.76 ms: 1.01x faster                                                     |
| scimark_monte_carlo      | 49.2 ms                                                               | 48.6 ms: 1.01x faster                                                     |
| html5lib                 | 33.0 ms                                                               | 32.6 ms: 1.01x faster                                                     |
| sympy_expand             | 252 ms                                                                | 249 ms: 1.01x faster                                                      |
| async_generators         | 297 ms                                                                | 294 ms: 1.01x faster                                                      |
| sympy_integrate          | 11.7 ms                                                               | 11.6 ms: 1.01x faster                                                     |
| async_tree_eager_tg      | 42.8 ms                                                               | 42.3 ms: 1.01x faster                                                     |
| chaos                    | 40.8 ms                                                               | 40.3 ms: 1.01x faster                                                     |
| pickle                   | 7.44 us                                                               | 7.37 us: 1.01x faster                                                     |
| unpickle                 | 9.35 us                                                               | 9.25 us: 1.01x faster                                                     |
| regex_effbot             | 2.48 ms                                                               | 2.46 ms: 1.01x faster                                                     |
| comprehensions           | 13.0 us                                                               | 12.8 us: 1.01x faster                                                     |
| thrift                   | 432 us                                                                | 428 us: 1.01x faster                                                      |
| nqueens                  | 58.9 ms                                                               | 58.3 ms: 1.01x faster                                                     |
| typing_runtime_protocols | 94.8 us                                                               | 94.0 us: 1.01x faster                                                     |
| pickle_pure_python       | 179 us                                                                | 177 us: 1.01x faster                                                      |
| sqlite_synth             | 1.59 us                                                               | 1.58 us: 1.01x faster                                                     |
| unpack_sequence          | 76.6 ns                                                               | 76.1 ns: 1.01x faster                                                     |
| tomli_loads              | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                                    |
| pprint_safe_repr         | 506 ms                                                                | 503 ms: 1.01x faster                                                      |
| async_tree_io            | 594 ms                                                                | 592 ms: 1.00x faster                                                      |
| sympy_sum                | 76.3 ms                                                               | 76.0 ms: 1.00x faster                                                     |
| dulwich_log              | 28.9 ms                                                               | 28.8 ms: 1.00x faster                                                     |
| deepcopy                 | 155 us                                                                | 155 us: 1.00x faster                                                      |
| crypto_pyaes             | 52.1 ms                                                               | 51.9 ms: 1.00x faster                                                     |
| nbody                    | 63.5 ms                                                               | 63.3 ms: 1.00x faster                                                     |
| bpe_tokeniser            | 3.08 sec                                                              | 3.09 sec: 1.00x slower                                                    |
| xml_etree_process        | 34.8 ms                                                               | 34.8 ms: 1.00x slower                                                     |
| unpickle_pure_python     | 131 us                                                                | 132 us: 1.00x slower                                                      |
| coroutines               | 16.0 ms                                                               | 16.0 ms: 1.00x slower                                                     |
| scimark_sor              | 88.6 ms                                                               | 88.9 ms: 1.00x slower                                                     |
| xml_etree_generate       | 51.0 ms                                                               | 51.2 ms: 1.00x slower                                                     |
| json_dumps               | 6.32 ms                                                               | 6.36 ms: 1.01x slower                                                     |
| bench_thread_pool        | 474 us                                                                | 477 us: 1.01x slower                                                      |
| coverage                 | 45.0 ms                                                               | 45.4 ms: 1.01x slower                                                     |
| create_gc_cycles         | 894 us                                                                | 903 us: 1.01x slower                                                      |
| pathlib                  | 23.8 ms                                                               | 24.2 ms: 1.02x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (40): tornado_http, pylint, async_tree_none, async_tree_cpu_io_mixed, sqlglot_parse, pprint_pformat, async_tree_none_tg, xml_etree_parse, bench_mp_pool, async_tree_io_tg, async_tree_memoization, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, json, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed_tg, deltablue, unpickle_list, json_loads, async_tree_eager_memoization_tg, pickle_dict, generators, python_startup_no_site, gc_traversal, asyncio_tcp_ssl, logging_silent, mako, asyncio_websockets, async_tree_cpu_io_mixed_tg, scimark_fft, raytrace, xml_etree_iterparse, spectral_norm, async_tree_eager_io, scimark_sparse_mat_mult, async_tree_eager_io_tg, float, pyflate, asyncio_tcp, python_startup

- Geometric mean (including insignificant results): 1.009x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x