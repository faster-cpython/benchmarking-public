# Results vs. 3.10.4

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: darwin-arm64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 0.61x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 176 ms: 1.09x faster                                                      |
| docutils       | 1.73 sec                                               | 1.56 sec: 1.11x faster                                                    |
| html5lib       | 42.4 ms                                                | 32.6 ms: 1.30x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 200 ms: 1.94x faster                                                      |
| async_tree_memoization  | 474 ms                                                 | 248 ms: 1.91x faster                                                      |
| async_tree_io           | 980 ms                                                 | 592 ms: 1.66x faster                                                      |
| async_tree_cpu_io_mixed | 649 ms                                                 | 462 ms: 1.40x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.6 ms: 1.48x faster                                                     |
| nbody          | 93.0 ms                                                | 63.3 ms: 1.47x faster                                                     |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.9 ms: 1.29x faster                                                     |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                      |
| regex_v8       | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 177 us: 1.58x faster                                                      |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.48x faster                                                      |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.38x faster                                                    |
| xml_etree_process    | 46.5 ms                                                | 34.8 ms: 1.34x faster                                                     |
| json_dumps           | 8.11 ms                                                | 6.36 ms: 1.27x faster                                                     |
| xml_etree_generate   | 53.5 ms                                                | 51.2 ms: 1.05x faster                                                     |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                                      |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                     |
| unpickle             | 8.80 us                                                | 9.25 us: 1.05x slower                                                     |
| pickle               | 6.97 us                                                | 7.37 us: 1.06x slower                                                     |
| pickle_list          | 2.74 us                                                | 2.94 us: 1.07x slower                                                     |
| unpickle_list        | 2.69 us                                                | 2.90 us: 1.08x slower                                                     |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.4 ms: 1.60x slower                                                     |
| python_startup_no_site | 7.91 ms                                                | 14.2 ms: 1.79x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.69x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                     |
| django_template | 26.4 ms                                                | 22.6 ms: 1.17x faster                                                     |
| genshi_text     | 17.3 ms                                                | 16.4 ms: 1.06x faster                                                     |
| genshi_xml      | 33.8 ms                                                | 40.4 ms: 1.19x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 94.0 us: 3.44x faster                                                     |
| deepcopy_memo            | 34.7 us                                                | 16.2 us: 2.15x faster                                                     |
| deltablue                | 4.91 ms                                                | 2.35 ms: 2.09x faster                                                     |
| async_tree_none          | 388 ms                                                 | 200 ms: 1.94x faster                                                      |
| async_tree_memoization   | 474 ms                                                 | 248 ms: 1.91x faster                                                      |
| logging_silent           | 117 ns                                                 | 62.5 ns: 1.88x faster                                                     |
| deepcopy                 | 272 us                                                 | 155 us: 1.76x faster                                                      |
| raytrace                 | 301 ms                                                 | 174 ms: 1.73x faster                                                      |
| async_tree_io            | 980 ms                                                 | 592 ms: 1.66x faster                                                      |
| chaos                    | 65.8 ms                                                | 40.3 ms: 1.63x faster                                                     |
| pickle_pure_python       | 281 us                                                 | 177 us: 1.58x faster                                                      |
| scimark_lu               | 103 ms                                                 | 65.2 ms: 1.58x faster                                                     |
| asyncio_tcp              | 659 ms                                                 | 424 ms: 1.56x faster                                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                     |
| mako                     | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                     |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                                      |
| float                    | 69.0 ms                                                | 46.6 ms: 1.48x faster                                                     |
| logging_simple           | 4.45 us                                                | 3.01 us: 1.48x faster                                                     |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.48x faster                                                      |
| nbody                    | 93.0 ms                                                | 63.3 ms: 1.47x faster                                                     |
| logging_format           | 4.83 us                                                | 3.30 us: 1.46x faster                                                     |
| sqlglot_parse            | 1.24 ms                                                | 858 us: 1.45x faster                                                      |
| scimark_sor              | 128 ms                                                 | 88.9 ms: 1.44x faster                                                     |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 462 ms: 1.40x faster                                                      |
| spectral_norm            | 94.8 ms                                                | 68.1 ms: 1.39x faster                                                     |
| crypto_pyaes             | 71.8 ms                                                | 51.9 ms: 1.39x faster                                                     |
| sqlglot_transpile        | 1.44 ms                                                | 1.04 ms: 1.38x faster                                                     |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.38x faster                                                    |
| scimark_monte_carlo      | 65.6 ms                                                | 48.6 ms: 1.35x faster                                                     |
| pylint                   | 277 ms                                                 | 206 ms: 1.35x faster                                                      |
| thrift                   | 572 us                                                 | 428 us: 1.34x faster                                                      |
| xml_etree_process        | 46.5 ms                                                | 34.8 ms: 1.34x faster                                                     |
| generators               | 32.3 ms                                                | 24.4 ms: 1.33x faster                                                     |
| comprehensions           | 16.9 us                                                | 12.8 us: 1.32x faster                                                     |
| hexiom                   | 6.19 ms                                                | 4.71 ms: 1.31x faster                                                     |
| html5lib                 | 42.4 ms                                                | 32.6 ms: 1.30x faster                                                     |
| pycparser                | 877 ms                                                 | 677 ms: 1.29x faster                                                      |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.29x faster                                                     |
| regex_compile            | 95.3 ms                                                | 73.9 ms: 1.29x faster                                                     |
| pyflate                  | 427 ms                                                 | 331 ms: 1.29x faster                                                      |
| json_dumps               | 8.11 ms                                                | 6.36 ms: 1.27x faster                                                     |
| pprint_safe_repr         | 641 ms                                                 | 503 ms: 1.27x faster                                                      |
| pprint_pformat           | 1.30 sec                                               | 1.03 sec: 1.27x faster                                                    |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                    |
| richards_super           | 57.8 ms                                                | 46.8 ms: 1.24x faster                                                     |
| dulwich_log              | 35.3 ms                                                | 28.8 ms: 1.23x faster                                                     |
| sympy_sum                | 92.2 ms                                                | 76.0 ms: 1.21x faster                                                     |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                      |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.17x faster                                                      |
| django_template          | 26.4 ms                                                | 22.6 ms: 1.17x faster                                                     |
| sympy_str                | 165 ms                                                 | 144 ms: 1.15x faster                                                      |
| sympy_integrate          | 13.1 ms                                                | 11.6 ms: 1.13x faster                                                     |
| fannkuch                 | 303 ms                                                 | 267 ms: 1.13x faster                                                      |
| mdp                      | 1.63 sec                                               | 1.45 sec: 1.13x faster                                                    |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.07 ms: 1.11x faster                                                     |
| docutils                 | 1.73 sec                                               | 1.56 sec: 1.11x faster                                                    |
| bench_thread_pool        | 527 us                                                 | 477 us: 1.11x faster                                                      |
| nqueens                  | 63.8 ms                                                | 58.3 ms: 1.09x faster                                                     |
| 2to3                     | 192 ms                                                 | 176 ms: 1.09x faster                                                      |
| richards                 | 48.7 ms                                                | 45.0 ms: 1.08x faster                                                     |
| sympy_expand             | 269 ms                                                 | 249 ms: 1.08x faster                                                      |
| genshi_text              | 17.3 ms                                                | 16.4 ms: 1.06x faster                                                     |
| json                     | 3.08 ms                                                | 2.95 ms: 1.05x faster                                                     |
| xml_etree_generate       | 53.5 ms                                                | 51.2 ms: 1.05x faster                                                     |
| meteor_contest           | 77.7 ms                                                | 74.6 ms: 1.04x faster                                                     |
| regex_v8                 | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                     |
| sqlglot_normalize        | 190 ms                                                 | 183 ms: 1.04x faster                                                      |
| sqlglot_optimize         | 36.8 ms                                                | 35.5 ms: 1.04x faster                                                     |
| pathlib                  | 24.5 ms                                                | 24.2 ms: 1.01x faster                                                     |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                      |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                      |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                                      |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                     |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                     |
| create_gc_cycles         | 860 us                                                 | 903 us: 1.05x slower                                                      |
| unpickle                 | 8.80 us                                                | 9.25 us: 1.05x slower                                                     |
| pickle                   | 6.97 us                                                | 7.37 us: 1.06x slower                                                     |
| pickle_list              | 2.74 us                                                | 2.94 us: 1.07x slower                                                     |
| unpickle_list            | 2.69 us                                                | 2.90 us: 1.08x slower                                                     |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                     |
| sqlite_synth             | 1.46 us                                                | 1.58 us: 1.08x slower                                                     |
| coverage                 | 41.5 ms                                                | 45.4 ms: 1.09x slower                                                     |
| genshi_xml               | 33.8 ms                                                | 40.4 ms: 1.19x slower                                                     |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                                      |
| telco                    | 3.49 ms                                                | 4.76 ms: 1.36x slower                                                     |
| bench_mp_pool            | 37.4 ms                                                | 52.2 ms: 1.40x slower                                                     |
| python_startup           | 10.9 ms                                                | 17.4 ms: 1.60x slower                                                     |
| python_startup_no_site   | 7.91 ms                                                | 14.2 ms: 1.79x slower                                                     |
| unpack_sequence          | 39.0 ns                                                | 76.1 ns: 1.95x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.20x faster                                                              |

Benchmark hidden because not significant (3): tornado_http, regex_effbot, xml_etree_iterparse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240910-3.14.0a0-8cbca05-JIT/bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 0.61x