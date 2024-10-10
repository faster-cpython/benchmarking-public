# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: windows-amd64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                        |
| chameleon      | 5.79 ms                                                     | 4.72 ms: 1.23x faster                                       |
| docutils       | 1.92 sec                                                    | 1.57 sec: 1.22x faster                                      |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                       |
| tornado_http   | 108 ms                                                      | 92.8 ms: 1.17x faster                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 521 ms: 2.13x faster                                        |
| async_tree_none         | 435 ms                                                      | 223 ms: 1.95x faster                                        |
| async_tree_memoization  | 526 ms                                                      | 271 ms: 1.94x faster                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 387 ms: 1.65x faster                                        |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.1 ms: 1.28x faster                                       |
| nbody          | 71.3 ms                                                     | 64.5 ms: 1.11x faster                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.1 ms: 1.32x faster                                       |
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                        |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.76 ms: 1.59x faster                                       |
| pickle_pure_python   | 270 us                                                      | 183 us: 1.47x faster                                        |
| unpickle_pure_python | 183 us                                                      | 127 us: 1.45x faster                                        |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                       |
| unpickle             | 9.09 us                                                     | 8.63 us: 1.05x faster                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.3 ms: 1.04x faster                                       |
| xml_etree_parse      | 96.8 ms                                                     | 93.2 ms: 1.04x faster                                       |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                       |
| pickle_dict          | 17.2 us                                                     | 18.0 us: 1.05x slower                                       |
| pickle_list          | 2.75 us                                                     | 2.89 us: 1.05x slower                                       |
| pickle               | 6.85 us                                                     | 7.34 us: 1.07x slower                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                       |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.24 ms: 1.45x faster                                       |
| genshi_text     | 19.8 ms                                                     | 14.9 ms: 1.33x faster                                       |
| django_template | 28.9 ms                                                     | 21.8 ms: 1.33x faster                                       |
| genshi_xml      | 41.0 ms                                                     | 32.8 ms: 1.25x faster                                       |
| Geometric mean  | (ref)                                                       | 1.34x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 100 us: 3.35x faster                                        |
| deltablue                | 4.19 ms                                                     | 1.86 ms: 2.25x faster                                       |
| async_tree_io            | 1.11 sec                                                    | 521 ms: 2.13x faster                                        |
| async_tree_none          | 435 ms                                                      | 223 ms: 1.95x faster                                        |
| async_tree_memoization   | 526 ms                                                      | 271 ms: 1.94x faster                                        |
| logging_silent           | 94.6 ns                                                     | 51.0 ns: 1.86x faster                                       |
| richards_super           | 52.2 ms                                                     | 29.3 ms: 1.78x faster                                       |
| raytrace                 | 273 ms                                                      | 156 ms: 1.75x faster                                        |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                       |
| pylint                   | 350 ms                                                      | 211 ms: 1.66x faster                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 387 ms: 1.65x faster                                        |
| go                       | 139 ms                                                      | 84.6 ms: 1.64x faster                                       |
| richards                 | 42.4 ms                                                     | 26.0 ms: 1.63x faster                                       |
| chaos                    | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                       |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 761 us: 1.60x faster                                        |
| json_dumps               | 9.16 ms                                                     | 5.76 ms: 1.59x faster                                       |
| scimark_lu               | 85.8 ms                                                     | 54.0 ms: 1.59x faster                                       |
| hexiom                   | 5.74 ms                                                     | 3.69 ms: 1.56x faster                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 952 us: 1.55x faster                                        |
| pyflate                  | 409 ms                                                      | 275 ms: 1.49x faster                                        |
| scimark_sor              | 106 ms                                                      | 72.0 ms: 1.47x faster                                       |
| pickle_pure_python       | 270 us                                                      | 183 us: 1.47x faster                                        |
| crypto_pyaes             | 62.5 ms                                                     | 42.8 ms: 1.46x faster                                       |
| mako                     | 9.03 ms                                                     | 6.24 ms: 1.45x faster                                       |
| unpickle_pure_python     | 183 us                                                      | 127 us: 1.45x faster                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.3 ms: 1.42x faster                                       |
| genshi_text              | 19.8 ms                                                     | 14.9 ms: 1.33x faster                                       |
| django_template          | 28.9 ms                                                     | 21.8 ms: 1.33x faster                                       |
| regex_compile            | 106 ms                                                      | 80.1 ms: 1.32x faster                                       |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.8 us: 1.32x faster                                       |
| spectral_norm            | 77.3 ms                                                     | 59.2 ms: 1.30x faster                                       |
| mypy2                    | 555 ms                                                      | 429 ms: 1.29x faster                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.64 sec: 1.29x faster                                      |
| mdp                      | 1.78 sec                                                    | 1.38 sec: 1.29x faster                                      |
| float                    | 61.7 ms                                                     | 48.1 ms: 1.28x faster                                       |
| coroutines               | 16.0 ms                                                     | 12.5 ms: 1.28x faster                                       |
| genshi_xml               | 41.0 ms                                                     | 32.8 ms: 1.25x faster                                       |
| dulwich_log              | 50.5 ms                                                     | 40.4 ms: 1.25x faster                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.25x faster                                       |
| sympy_sum                | 107 ms                                                      | 86.4 ms: 1.24x faster                                       |
| pprint_pformat           | 1.22 sec                                                    | 991 ms: 1.23x faster                                        |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                      |
| pycparser                | 930 ms                                                      | 758 ms: 1.23x faster                                        |
| chameleon                | 5.79 ms                                                     | 4.72 ms: 1.23x faster                                       |
| docutils                 | 1.92 sec                                                    | 1.57 sec: 1.22x faster                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 33.1 ms: 1.20x faster                                       |
| pprint_safe_repr         | 592 ms                                                      | 493 ms: 1.20x faster                                        |
| nqueens                  | 66.6 ms                                                     | 55.5 ms: 1.20x faster                                       |
| sqlglot_normalize        | 205 ms                                                      | 171 ms: 1.20x faster                                        |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                       |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                        |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                        |
| tornado_http             | 108 ms                                                      | 92.8 ms: 1.17x faster                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.34 ms: 1.16x faster                                       |
| bench_thread_pool        | 958 us                                                      | 828 us: 1.16x faster                                        |
| deepcopy                 | 255 us                                                      | 223 us: 1.14x faster                                        |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                        |
| asyncio_tcp              | 732 ms                                                      | 654 ms: 1.12x faster                                        |
| nbody                    | 71.3 ms                                                     | 64.5 ms: 1.11x faster                                       |
| sympy_expand             | 314 ms                                                      | 285 ms: 1.10x faster                                        |
| logging_format           | 6.76 us                                                     | 6.15 us: 1.10x faster                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                       |
| logging_simple           | 6.22 us                                                     | 5.72 us: 1.09x faster                                       |
| scimark_fft              | 187 ms                                                      | 174 ms: 1.07x faster                                        |
| aiohttp                  | 995 us                                                      | 932 us: 1.07x faster                                        |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                       |
| unpickle                 | 9.09 us                                                     | 8.63 us: 1.05x faster                                       |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                       |
| meteor_contest           | 75.9 ms                                                     | 72.3 ms: 1.05x faster                                       |
| fannkuch                 | 256 ms                                                      | 245 ms: 1.04x faster                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.3 ms: 1.04x faster                                       |
| xml_etree_parse          | 96.8 ms                                                     | 93.2 ms: 1.04x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.00x faster                                        |
| async_generators         | 222 ms                                                      | 223 ms: 1.01x slower                                        |
| flaskblogging            | 2.03 sec                                                    | 2.04 sec: 1.01x slower                                      |
| unpack_sequence          | 39.6 ns                                                     | 40.0 ns: 1.01x slower                                       |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                       |
| create_gc_cycles         | 800 us                                                      | 829 us: 1.04x slower                                        |
| pickle_dict              | 17.2 us                                                     | 18.0 us: 1.05x slower                                       |
| pickle_list              | 2.75 us                                                     | 2.89 us: 1.05x slower                                       |
| pickle                   | 6.85 us                                                     | 7.34 us: 1.07x slower                                       |
| pathlib                  | 75.7 ms                                                     | 81.2 ms: 1.07x slower                                       |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                       |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                       |
| bench_mp_pool            | 62.0 ms                                                     | 69.6 ms: 1.12x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                       |
| coverage                 | 39.0 ms                                                     | 46.7 ms: 1.20x slower                                       |
| telco                    | 3.94 ms                                                     | 4.85 ms: 1.23x slower                                       |
| thrift                   | 617 us                                                      | 8.68 ms: 14.06x slower                                      |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown