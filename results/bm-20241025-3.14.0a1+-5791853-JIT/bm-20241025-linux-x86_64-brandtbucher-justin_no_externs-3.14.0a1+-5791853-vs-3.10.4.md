# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.362x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 283 ms: 1.23x faster                                                      |
| docutils       | 3.30 sec                                               | 2.94 sec: 1.12x faster                                                    |
| html5lib       | 88.9 ms                                                | 66.0 ms: 1.35x faster                                                     |
| tornado_http   | 136 ms                                                 | 95.0 ms: 1.43x faster                                                     |
| Geometric mean | (ref)                                                  | 1.28x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 341 ms: 2.13x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 418 ms: 2.08x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 856 ms: 2.07x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 583 ms: 1.74x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.2 ms: 1.72x faster                                                     |
| float          | 117 ms                                                 | 77.8 ms: 1.51x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.34x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                     |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 57.4 ms: 1.38x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                     |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.14x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.23x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.55x faster                                                     |
| django_template | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 60.5 ms: 1.09x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.14x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.44 ms: 2.30x faster                                                     |
| generators               | 80.1 ms                                                | 36.4 ms: 2.20x faster                                                     |
| async_tree_none          | 728 ms                                                 | 341 ms: 2.13x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 418 ms: 2.08x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 856 ms: 2.07x faster                                                      |
| richards_super           | 94.7 ms                                                | 48.5 ms: 1.95x faster                                                     |
| chaos                    | 115 ms                                                 | 61.9 ms: 1.87x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 31.8 us: 1.84x faster                                                     |
| richards                 | 79.3 ms                                                | 44.8 ms: 1.77x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 72.6 ms: 1.76x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 583 ms: 1.74x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                     |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                      |
| go                       | 240 ms                                                 | 139 ms: 1.73x faster                                                      |
| deepcopy                 | 479 us                                                 | 278 us: 1.73x faster                                                      |
| nbody                    | 154 ms                                                 | 89.2 ms: 1.72x faster                                                     |
| raytrace                 | 507 ms                                                 | 295 ms: 1.72x faster                                                      |
| logging_silent           | 190 ns                                                 | 112 ns: 1.70x faster                                                      |
| pylint                   | 551 ms                                                 | 326 ms: 1.69x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.36 ms: 1.60x faster                                                     |
| comprehensions           | 28.8 us                                                | 18.0 us: 1.59x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                    |
| pyflate                  | 716 ms                                                 | 457 ms: 1.57x faster                                                      |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.55x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                     |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.71 ms: 1.51x faster                                                     |
| float                    | 117 ms                                                 | 77.8 ms: 1.51x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                     |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.84 us: 1.47x faster                                                     |
| tornado_http             | 136 ms                                                 | 95.0 ms: 1.43x faster                                                     |
| spectral_norm            | 170 ms                                                 | 121 ms: 1.40x faster                                                      |
| scimark_fft              | 466 ms                                                 | 333 ms: 1.40x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.45 ms: 1.40x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 57.4 ms: 1.38x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                                     |
| html5lib                 | 88.9 ms                                                | 66.0 ms: 1.35x faster                                                     |
| thrift                   | 1.07 ms                                                | 801 us: 1.34x faster                                                      |
| regex_compile            | 188 ms                                                 | 141 ms: 1.34x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                    |
| django_template          | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.9 ms: 1.30x faster                                                     |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 67.7 ms: 1.25x faster                                                     |
| genshi_text              | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                     |
| 2to3                     | 348 ms                                                 | 283 ms: 1.23x faster                                                      |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.23x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 118 ms: 1.22x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 147 ms: 1.17x faster                                                      |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                     |
| json                     | 5.69 ms                                                | 5.00 ms: 1.14x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 60.8 ms: 1.14x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.14x faster                                                      |
| sympy_str                | 346 ms                                                 | 306 ms: 1.13x faster                                                      |
| nqueens                  | 106 ms                                                 | 93.8 ms: 1.13x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.94 sec: 1.12x faster                                                    |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.12x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                     |
| sympy_sum                | 196 ms                                                 | 178 ms: 1.11x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 893 us: 1.11x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 60.5 ms: 1.09x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 23.8 ms: 1.09x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                                    |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                      |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                      |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                      |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                      |
| coverage                 | 79.4 ms                                                | 83.7 ms: 1.05x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                     |
| telco                    | 7.27 ms                                                | 7.99 ms: 1.10x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.74 ms: 1.31x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 84.3 ms: 3.51x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                              |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241025-3.14.0a1+-5791853-JIT/bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.362x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.33x