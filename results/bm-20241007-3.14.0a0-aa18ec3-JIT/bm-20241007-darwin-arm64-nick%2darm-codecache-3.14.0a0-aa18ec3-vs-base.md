# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 180 ms                                                                | 169 ms: 1.07x faster                                           |
| docutils       | 1.58 sec                                                              | 1.49 sec: 1.06x faster                                         |
| html5lib       | 34.3 ms                                                               | 32.6 ms: 1.05x faster                                          |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_eager    | 63.1 ms                                                               | 61.7 ms: 1.02x faster                                          |
| async_generators    | 290 ms                                                                | 289 ms: 1.00x faster                                           |
| asyncio_websockets  | 241 ms                                                                | 242 ms: 1.00x slower                                           |
| coroutines          | 16.2 ms                                                               | 16.3 ms: 1.00x slower                                          |
| async_tree_eager_tg | 41.3 ms                                                               | 41.4 ms: 1.00x slower                                          |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (16): asyncio_tcp, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_eager_io, async_tree_io_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_eager_cpu_io_mixed_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 282 ms                                                                | 282 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 75.7 ms                                                               | 71.6 ms: 1.06x faster                                          |
| regex_effbot   | 2.68 ms                                                               | 2.64 ms: 1.02x faster                                          |
| regex_v8       | 16.9 ms                                                               | 16.8 ms: 1.00x faster                                          |
| regex_dna      | 147 ms                                                                | 149 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_process    | 34.7 ms                                                               | 33.7 ms: 1.03x faster                                          |
| xml_etree_generate   | 50.4 ms                                                               | 49.1 ms: 1.02x faster                                          |
| pickle_list          | 2.99 us                                                               | 2.94 us: 1.02x faster                                          |
| json_loads           | 16.5 us                                                               | 16.3 us: 1.01x faster                                          |
| tomli_loads          | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                         |
| json_dumps           | 6.12 ms                                                               | 6.10 ms: 1.00x faster                                          |
| pickle_dict          | 18.1 us                                                               | 18.1 us: 1.00x faster                                          |
| unpickle_pure_python | 130 us                                                                | 130 us: 1.00x faster                                           |
| pickle               | 7.41 us                                                               | 7.44 us: 1.00x slower                                          |
| unpickle             | 9.02 us                                                               | 9.07 us: 1.01x slower                                          |
| unpickle_list        | 2.97 us                                                               | 3.02 us: 1.02x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 42.5 ms                                                               | 32.1 ms: 1.32x faster                                          |
| django_template | 23.2 ms                                                               | 20.2 ms: 1.15x faster                                          |
| genshi_text     | 16.6 ms                                                               | 14.6 ms: 1.14x faster                                          |
| Geometric mean  | (ref)                                                                 | 1.15x faster                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| richards                 | 45.2 ms                                                               | 30.6 ms: 1.48x faster                                          |
| richards_super           | 46.9 ms                                                               | 34.0 ms: 1.38x faster                                          |
| genshi_xml               | 42.5 ms                                                               | 32.1 ms: 1.32x faster                                          |
| django_template          | 23.2 ms                                                               | 20.2 ms: 1.15x faster                                          |
| genshi_text              | 16.6 ms                                                               | 14.6 ms: 1.14x faster                                          |
| sqlglot_optimize         | 37.7 ms                                                               | 33.8 ms: 1.11x faster                                          |
| go                       | 101 ms                                                                | 93.4 ms: 1.08x faster                                          |
| sqlglot_normalize        | 187 ms                                                                | 174 ms: 1.07x faster                                           |
| sympy_integrate          | 12.6 ms                                                               | 11.7 ms: 1.07x faster                                          |
| sqlglot_transpile        | 1.05 ms                                                               | 980 us: 1.07x faster                                           |
| 2to3                     | 180 ms                                                                | 169 ms: 1.07x faster                                           |
| pprint_safe_repr         | 491 ms                                                                | 462 ms: 1.06x faster                                           |
| sympy_str                | 150 ms                                                                | 141 ms: 1.06x faster                                           |
| hexiom                   | 4.70 ms                                                               | 4.42 ms: 1.06x faster                                          |
| docutils                 | 1.58 sec                                                              | 1.49 sec: 1.06x faster                                         |
| regex_compile            | 75.7 ms                                                               | 71.6 ms: 1.06x faster                                          |
| sqlglot_parse            | 849 us                                                                | 804 us: 1.06x faster                                           |
| html5lib                 | 34.3 ms                                                               | 32.6 ms: 1.05x faster                                          |
| deepcopy                 | 156 us                                                                | 148 us: 1.05x faster                                           |
| sympy_sum                | 77.9 ms                                                               | 74.0 ms: 1.05x faster                                          |
| sympy_expand             | 247 ms                                                                | 235 ms: 1.05x faster                                           |
| pycparser                | 678 ms                                                                | 649 ms: 1.04x faster                                           |
| generators               | 25.0 ms                                                               | 24.1 ms: 1.04x faster                                          |
| scimark_monte_carlo      | 47.7 ms                                                               | 46.1 ms: 1.03x faster                                          |
| comprehensions           | 12.9 us                                                               | 12.5 us: 1.03x faster                                          |
| thrift                   | 427 us                                                                | 415 us: 1.03x faster                                           |
| xml_etree_process        | 34.7 ms                                                               | 33.7 ms: 1.03x faster                                          |
| meteor_contest           | 75.5 ms                                                               | 73.5 ms: 1.03x faster                                          |
| raytrace                 | 176 ms                                                                | 171 ms: 1.03x faster                                           |
| xml_etree_generate       | 50.4 ms                                                               | 49.1 ms: 1.02x faster                                          |
| chaos                    | 40.7 ms                                                               | 39.7 ms: 1.02x faster                                          |
| async_tree_eager         | 63.1 ms                                                               | 61.7 ms: 1.02x faster                                          |
| logging_format           | 3.38 us                                                               | 3.31 us: 1.02x faster                                          |
| pprint_pformat           | 998 ms                                                                | 979 ms: 1.02x faster                                           |
| logging_simple           | 3.10 us                                                               | 3.04 us: 1.02x faster                                          |
| dulwich_log              | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                          |
| regex_effbot             | 2.68 ms                                                               | 2.64 ms: 1.02x faster                                          |
| pickle_list              | 2.99 us                                                               | 2.94 us: 1.02x faster                                          |
| pyflate                  | 322 ms                                                                | 317 ms: 1.02x faster                                           |
| typing_runtime_protocols | 95.7 us                                                               | 94.5 us: 1.01x faster                                          |
| crypto_pyaes             | 52.4 ms                                                               | 51.8 ms: 1.01x faster                                          |
| json_loads               | 16.5 us                                                               | 16.3 us: 1.01x faster                                          |
| tomli_loads              | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                         |
| unpack_sequence          | 75.8 ns                                                               | 74.9 ns: 1.01x faster                                          |
| pathlib                  | 22.0 ms                                                               | 21.8 ms: 1.01x faster                                          |
| deltablue                | 2.38 ms                                                               | 2.36 ms: 1.01x faster                                          |
| scimark_fft              | 185 ms                                                                | 184 ms: 1.01x faster                                           |
| mdp                      | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                         |
| deepcopy_reduce          | 1.52 us                                                               | 1.51 us: 1.01x faster                                          |
| scimark_sor              | 87.5 ms                                                               | 87.0 ms: 1.01x faster                                          |
| regex_v8                 | 16.9 ms                                                               | 16.8 ms: 1.00x faster                                          |
| sqlite_synth             | 1.54 us                                                               | 1.53 us: 1.00x faster                                          |
| json_dumps               | 6.12 ms                                                               | 6.10 ms: 1.00x faster                                          |
| async_generators         | 290 ms                                                                | 289 ms: 1.00x faster                                           |
| pickle_dict              | 18.1 us                                                               | 18.1 us: 1.00x faster                                          |
| unpickle_pure_python     | 130 us                                                                | 130 us: 1.00x faster                                           |
| bpe_tokeniser            | 3.06 sec                                                              | 3.06 sec: 1.00x faster                                         |
| pidigits                 | 282 ms                                                                | 282 ms: 1.00x slower                                           |
| asyncio_websockets       | 241 ms                                                                | 242 ms: 1.00x slower                                           |
| spectral_norm            | 66.8 ms                                                               | 66.9 ms: 1.00x slower                                          |
| coroutines               | 16.2 ms                                                               | 16.3 ms: 1.00x slower                                          |
| gc_traversal             | 2.47 ms                                                               | 2.48 ms: 1.00x slower                                          |
| async_tree_eager_tg      | 41.3 ms                                                               | 41.4 ms: 1.00x slower                                          |
| pickle                   | 7.41 us                                                               | 7.44 us: 1.00x slower                                          |
| unpickle                 | 9.02 us                                                               | 9.07 us: 1.01x slower                                          |
| regex_dna                | 147 ms                                                                | 149 ms: 1.01x slower                                           |
| unpickle_list            | 2.97 us                                                               | 3.02 us: 1.02x slower                                          |
| coverage                 | 43.8 ms                                                               | 44.6 ms: 1.02x slower                                          |
| scimark_sparse_mat_mult  | 2.97 ms                                                               | 3.03 ms: 1.02x slower                                          |
| bench_thread_pool        | 462 us                                                                | 478 us: 1.03x slower                                           |
| Geometric mean           | (ref)                                                                 | 1.03x faster                                                   |

Benchmark hidden because not significant (35): pylint, tornado_http, asyncio_tcp, async_tree_eager_memoization, json, bench_mp_pool, async_tree_eager_memoization_tg, async_tree_eager_io_tg, python_startup, xml_etree_parse, async_tree_eager_io, async_tree_io_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, xml_etree_iterparse, async_tree_cpu_io_mixed, deepcopy_memo, async_tree_none_tg, async_tree_cpu_io_mixed_tg, create_gc_cycles, async_tree_io, pickle_pure_python, fannkuch, telco, nbody, async_tree_memoization, async_tree_none, logging_silent, nqueens, float, scimark_lu, mako, async_tree_eager_cpu_io_mixed_tg, python_startup_no_site, asyncio_tcp_ssl

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x