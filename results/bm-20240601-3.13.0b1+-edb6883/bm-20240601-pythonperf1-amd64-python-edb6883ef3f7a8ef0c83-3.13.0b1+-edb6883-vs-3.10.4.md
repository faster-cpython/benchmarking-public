# Results vs. 3.10.4

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: windows-amd64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 208 ms: 1.18x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.86 ms: 1.19x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                      |
| html5lib       | 51.0 ms                                                     | 35.4 ms: 1.44x faster                                                       |
| tornado_http   | 108 ms                                                      | 82.0 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 219 ms: 1.98x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 268 ms: 1.96x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 594 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.86x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 49.7 ms: 1.24x faster                                                       |
| nbody          | 71.3 ms                                                     | 70.9 ms: 1.01x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.9 ms: 1.36x faster                                                       |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.62 ms: 1.63x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 179 us: 1.51x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 125 us: 1.46x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.40 us: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.1 ms: 1.05x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.01x faster                                                       |
| pickle               | 6.85 us                                                     | 7.20 us: 1.05x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.92 us: 1.06x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.5 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.1 ms: 1.02x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.1 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.51 ms: 1.39x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 14.7 ms: 1.34x faster                                                       |
| django_template | 28.9 ms                                                     | 21.8 ms: 1.32x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 31.9 ms: 1.29x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.94 ms: 2.16x faster                                                       |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.98x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 268 ms: 1.96x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 594 ms: 1.87x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 54.1 ns: 1.75x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.4 ms: 1.72x faster                                                       |
| pylint                   | 350 ms                                                      | 204 ms: 1.72x faster                                                        |
| raytrace                 | 273 ms                                                      | 160 ms: 1.71x faster                                                        |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.69x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                        |
| go                       | 139 ms                                                      | 84.5 ms: 1.64x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.62 ms: 1.63x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.3 ms: 1.61x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 759 us: 1.60x faster                                                        |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.59x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.2 ms: 1.58x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 472 ms: 1.55x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 3.77 ms: 1.52x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 969 us: 1.52x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 179 us: 1.51x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.46x faster                                                        |
| pyflate                  | 409 ms                                                      | 283 ms: 1.45x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 35.4 ms: 1.44x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.48 sec: 1.43x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.51 ms: 1.39x faster                                                       |
| scimark_sor              | 106 ms                                                      | 76.8 ms: 1.38x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.5 ms: 1.38x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.8 ms: 1.36x faster                                                       |
| regex_compile            | 106 ms                                                      | 77.9 ms: 1.36x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.7 ms: 1.34x faster                                                       |
| mypy2                    | 555 ms                                                      | 418 ms: 1.33x faster                                                        |
| django_template          | 28.9 ms                                                     | 21.8 ms: 1.32x faster                                                       |
| tornado_http             | 108 ms                                                      | 82.0 ms: 1.32x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 38.7 ms: 1.31x faster                                                       |
| pycparser                | 930 ms                                                      | 717 ms: 1.30x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 31.9 ms: 1.29x faster                                                       |
| sympy_sum                | 107 ms                                                      | 83.5 ms: 1.28x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 22.5 us: 1.28x faster                                                       |
| coroutines               | 16.0 ms                                                     | 12.7 ms: 1.26x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                       |
| float                    | 61.7 ms                                                     | 49.7 ms: 1.24x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 787 us: 1.22x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 63.9 ms: 1.21x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                      |
| sympy_str                | 194 ms                                                      | 161 ms: 1.21x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 494 ms: 1.20x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 33.3 ms: 1.19x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                      |
| chameleon                | 5.79 ms                                                     | 4.86 ms: 1.19x faster                                                       |
| 2to3                     | 246 ms                                                      | 208 ms: 1.18x faster                                                        |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 56.6 ms: 1.18x faster                                                       |
| deepcopy                 | 255 us                                                      | 218 us: 1.17x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 176 ms: 1.16x faster                                                        |
| sympy_expand             | 314 ms                                                      | 273 ms: 1.15x faster                                                        |
| aiohttp                  | 995 us                                                      | 885 us: 1.12x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.98 us: 1.11x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.20 us: 1.09x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.40 us: 1.08x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.83 us: 1.07x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.56 ms: 1.06x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.1 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                                       |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.05x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.1 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 249 ms: 1.03x faster                                                        |
| scimark_fft              | 187 ms                                                      | 182 ms: 1.03x faster                                                        |
| python_startup           | 20.6 ms                                                     | 20.1 ms: 1.02x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.01x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 74.8 ms: 1.01x faster                                                       |
| nbody                    | 71.3 ms                                                     | 70.9 ms: 1.01x faster                                                       |
| flaskblogging            | 2.03 sec                                                    | 2.04 sec: 1.00x slower                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| async_generators         | 222 ms                                                      | 224 ms: 1.01x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 16.1 ms: 1.04x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 64.8 ms: 1.04x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.20 us: 1.05x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.92 us: 1.06x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.5 us: 1.08x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                       |
| coverage                 | 39.0 ms                                                     | 43.4 ms: 1.11x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 907 us: 1.13x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.62 ms: 1.17x slower                                                       |
| thrift                   | 617 us                                                      | 8.05 ms: 13.04x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, regex_v8
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown