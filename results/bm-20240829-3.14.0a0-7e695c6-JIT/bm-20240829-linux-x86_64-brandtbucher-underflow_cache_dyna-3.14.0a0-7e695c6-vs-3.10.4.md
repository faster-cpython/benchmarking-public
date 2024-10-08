# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_cache_dyna
- machine: linux-x86_64
- commit hash: 7e695c6
- commit date: 2024-08-29
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.23x faster                                                        |
| html5lib       | 88.9 ms                                                | 76.2 ms: 1.17x faster                                                       |
| tornado_http   | 136 ms                                                 | 99.5 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 411 ms: 2.12x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 936 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.3 ms: 1.94x faster                                                       |
| float          | 117 ms                                                 | 71.1 ms: 1.65x faster                                                       |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 154 ms: 1.22x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                       |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 203 us: 1.63x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 54.8 ms: 1.44x faster                                                       |
| json_dumps           | 14.2 ms                                                | 9.94 ms: 1.43x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 77.1 ms: 1.29x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| json_loads           | 31.2 us                                                | 29.5 us: 1.06x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.74 ms: 1.68x faster                                                       |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                       |
| django_template | 48.2 ms                                                | 38.9 ms: 1.24x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 64.0 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                       |
| generators               | 80.1 ms                                                | 34.3 ms: 2.33x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 26.1 us: 2.24x faster                                                       |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 411 ms: 2.12x faster                                                        |
| richards_super           | 94.7 ms                                                | 45.8 ms: 2.07x faster                                                       |
| logging_silent           | 190 ns                                                 | 94.7 ns: 2.00x faster                                                       |
| richards                 | 79.3 ms                                                | 40.4 ms: 1.96x faster                                                       |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                       |
| nbody                    | 154 ms                                                 | 79.3 ms: 1.94x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 61.7 ms: 1.92x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 67.5 ms: 1.89x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 936 ms: 1.89x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 503 ms: 1.83x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                                        |
| raytrace                 | 507 ms                                                 | 282 ms: 1.80x faster                                                        |
| deepcopy                 | 479 us                                                 | 267 us: 1.80x faster                                                        |
| scimark_lu               | 176 ms                                                 | 101 ms: 1.75x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                       |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.69x faster                                                        |
| mako                     | 16.3 ms                                                | 9.74 ms: 1.68x faster                                                       |
| float                    | 117 ms                                                 | 71.1 ms: 1.65x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 203 us: 1.63x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                      |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                       |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.04 ms: 1.48x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.40 ms: 1.47x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.73 us: 1.45x faster                                                       |
| logging_format           | 9.09 us                                                | 6.29 us: 1.44x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 54.8 ms: 1.44x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.80 ms: 1.43x faster                                                       |
| scimark_sor              | 220 ms                                                 | 154 ms: 1.43x faster                                                        |
| json_dumps               | 14.2 ms                                                | 9.94 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.53 ms: 1.42x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                                        |
| fannkuch                 | 532 ms                                                 | 380 ms: 1.40x faster                                                        |
| go                       | 240 ms                                                 | 173 ms: 1.39x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                       |
| tornado_http             | 136 ms                                                 | 99.5 ms: 1.37x faster                                                       |
| pylint                   | 551 ms                                                 | 406 ms: 1.36x faster                                                        |
| thrift                   | 1.07 ms                                                | 795 us: 1.35x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 77.1 ms: 1.29x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                       |
| nqueens                  | 106 ms                                                 | 83.8 ms: 1.26x faster                                                       |
| django_template          | 48.2 ms                                                | 38.9 ms: 1.24x faster                                                       |
| 2to3                     | 348 ms                                                 | 282 ms: 1.23x faster                                                        |
| regex_compile            | 188 ms                                                 | 154 ms: 1.22x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 120 ms: 1.19x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 830 us: 1.19x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                       |
| html5lib                 | 88.9 ms                                                | 76.2 ms: 1.17x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 59.7 ms: 1.16x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                      |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.42 sec: 1.11x faster                                                      |
| sympy_sum                | 196 ms                                                 | 180 ms: 1.09x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 23.7 ms: 1.09x faster                                                       |
| sympy_str                | 346 ms                                                 | 321 ms: 1.08x faster                                                        |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                       |
| sympy_expand             | 566 ms                                                 | 528 ms: 1.07x faster                                                        |
| json_loads               | 31.2 us                                                | 29.5 us: 1.06x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 64.0 ms: 1.03x faster                                                       |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                        |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                       |
| async_generators         | 444 ms                                                 | 465 ms: 1.05x slower                                                        |
| telco                    | 7.27 ms                                                | 7.69 ms: 1.06x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                       |
| coverage                 | 79.4 ms                                                | 87.4 ms: 1.10x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, docutils
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-7e695c6-JIT/bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.23x