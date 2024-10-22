# Results vs. 3.13.0

- fork: python
- ref: v3.10.4
- machine: windows-amd64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.22x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 246 ms: 1.13x slower                                        |
| chameleon      | 4.72 ms                                                     | 5.79 ms: 1.23x slower                                       |
| docutils       | 1.57 sec                                                    | 1.92 sec: 1.22x slower                                      |
| html5lib       | 38.6 ms                                                     | 51.0 ms: 1.32x slower                                       |
| tornado_http   | 92.8 ms                                                     | 108 ms: 1.17x slower                                        |
| Geometric mean | (ref)                                                       | 1.21x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_generators        | 223 ms                                                      | 222 ms: 1.01x faster                                        |
| asyncio_tcp             | 654 ms                                                      | 732 ms: 1.12x slower                                        |
| coroutines              | 12.5 ms                                                     | 16.0 ms: 1.28x slower                                       |
| asyncio_tcp_ssl         | 1.64 sec                                                    | 2.11 sec: 1.29x slower                                      |
| async_tree_cpu_io_mixed | 387 ms                                                      | 638 ms: 1.65x slower                                        |
| async_tree_memoization  | 271 ms                                                      | 526 ms: 1.94x slower                                        |
| async_tree_none         | 223 ms                                                      | 435 ms: 1.95x slower                                        |
| async_tree_io           | 521 ms                                                      | 1.11 sec: 2.13x slower                                      |
| Geometric mean          | (ref)                                                       | 1.49x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 149 ms: 1.00x slower                                        |
| nbody          | 64.5 ms                                                     | 71.3 ms: 1.11x slower                                       |
| float          | 48.1 ms                                                     | 61.7 ms: 1.28x slower                                       |
| Geometric mean | (ref)                                                       | 1.13x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                       |
| regex_v8       | 14.7 ms                                                     | 15.4 ms: 1.05x slower                                       |
| regex_dna      | 114 ms                                                      | 136 ms: 1.19x slower                                        |
| regex_compile  | 80.1 ms                                                     | 106 ms: 1.32x slower                                        |
| Geometric mean | (ref)                                                       | 1.14x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 6.85 us: 1.07x faster                                       |
| pickle_list          | 2.89 us                                                     | 2.75 us: 1.05x faster                                       |
| pickle_dict          | 18.0 us                                                     | 17.2 us: 1.05x faster                                       |
| json_loads           | 14.3 us                                                     | 14.0 us: 1.02x faster                                       |
| xml_etree_parse      | 93.2 ms                                                     | 96.8 ms: 1.04x slower                                       |
| xml_etree_generate   | 53.3 ms                                                     | 55.5 ms: 1.04x slower                                       |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.0 ms: 1.04x slower                                       |
| unpickle             | 8.63 us                                                     | 9.09 us: 1.05x slower                                       |
| xml_etree_process    | 36.5 ms                                                     | 44.5 ms: 1.22x slower                                       |
| tomli_loads          | 1.36 sec                                                    | 1.67 sec: 1.23x slower                                      |
| unpickle_pure_python | 127 us                                                      | 183 us: 1.45x slower                                        |
| pickle_pure_python   | 183 us                                                      | 270 us: 1.47x slower                                        |
| json_dumps           | 5.76 ms                                                     | 9.16 ms: 1.59x slower                                       |
| Geometric mean       | (ref)                                                       | 1.12x slower                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 15.5 ms: 1.15x faster                                       |
| python_startup         | 22.2 ms                                                     | 20.6 ms: 1.08x faster                                       |
| Geometric mean         | (ref)                                                       | 1.11x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 41.0 ms: 1.25x slower                                       |
| django_template | 21.8 ms                                                     | 28.9 ms: 1.33x slower                                       |
| genshi_text     | 14.9 ms                                                     | 19.8 ms: 1.33x slower                                       |
| mako            | 6.24 ms                                                     | 9.03 ms: 1.45x slower                                       |
| Geometric mean  | (ref)                                                       | 1.34x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| thrift                   | 8.68 ms                                                     | 617 us: 14.06x faster                                       |
| telco                    | 4.85 ms                                                     | 3.94 ms: 1.23x faster                                       |
| coverage                 | 46.7 ms                                                     | 39.0 ms: 1.20x faster                                       |
| python_startup_no_site   | 17.8 ms                                                     | 15.5 ms: 1.15x faster                                       |
| bench_mp_pool            | 69.6 ms                                                     | 62.0 ms: 1.12x faster                                       |
| gc_traversal             | 1.55 ms                                                     | 1.41 ms: 1.10x faster                                       |
| python_startup           | 22.2 ms                                                     | 20.6 ms: 1.08x faster                                       |
| pathlib                  | 81.2 ms                                                     | 75.7 ms: 1.07x faster                                       |
| pickle                   | 7.34 us                                                     | 6.85 us: 1.07x faster                                       |
| pickle_list              | 2.89 us                                                     | 2.75 us: 1.05x faster                                       |
| pickle_dict              | 18.0 us                                                     | 17.2 us: 1.05x faster                                       |
| create_gc_cycles         | 829 us                                                      | 800 us: 1.04x faster                                        |
| json_loads               | 14.3 us                                                     | 14.0 us: 1.02x faster                                       |
| unpack_sequence          | 40.0 ns                                                     | 39.6 ns: 1.01x faster                                       |
| flaskblogging            | 2.04 sec                                                    | 2.03 sec: 1.01x faster                                      |
| async_generators         | 223 ms                                                      | 222 ms: 1.01x faster                                        |
| pidigits                 | 148 ms                                                      | 149 ms: 1.00x slower                                        |
| regex_effbot             | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                       |
| xml_etree_parse          | 93.2 ms                                                     | 96.8 ms: 1.04x slower                                       |
| xml_etree_generate       | 53.3 ms                                                     | 55.5 ms: 1.04x slower                                       |
| xml_etree_iterparse      | 62.3 ms                                                     | 65.0 ms: 1.04x slower                                       |
| fannkuch                 | 245 ms                                                      | 256 ms: 1.04x slower                                        |
| meteor_contest           | 72.3 ms                                                     | 75.9 ms: 1.05x slower                                       |
| json                     | 2.98 ms                                                     | 3.14 ms: 1.05x slower                                       |
| unpickle                 | 8.63 us                                                     | 9.09 us: 1.05x slower                                       |
| regex_v8                 | 14.7 ms                                                     | 15.4 ms: 1.05x slower                                       |
| aiohttp                  | 932 us                                                      | 995 us: 1.07x slower                                        |
| scimark_fft              | 174 ms                                                      | 187 ms: 1.07x slower                                        |
| logging_simple           | 5.72 us                                                     | 6.22 us: 1.09x slower                                       |
| deepcopy_reduce          | 2.02 us                                                     | 2.20 us: 1.09x slower                                       |
| logging_format           | 6.15 us                                                     | 6.76 us: 1.10x slower                                       |
| sympy_expand             | 285 ms                                                      | 314 ms: 1.10x slower                                        |
| nbody                    | 64.5 ms                                                     | 71.3 ms: 1.11x slower                                       |
| asyncio_tcp              | 654 ms                                                      | 732 ms: 1.12x slower                                        |
| 2to3                     | 217 ms                                                      | 246 ms: 1.13x slower                                        |
| deepcopy                 | 223 us                                                      | 255 us: 1.14x slower                                        |
| bench_thread_pool        | 828 us                                                      | 958 us: 1.16x slower                                        |
| scimark_sparse_mat_mult  | 2.34 ms                                                     | 2.72 ms: 1.16x slower                                       |
| tornado_http             | 92.8 ms                                                     | 108 ms: 1.17x slower                                        |
| sympy_str                | 166 ms                                                      | 194 ms: 1.17x slower                                        |
| regex_dna                | 114 ms                                                      | 136 ms: 1.19x slower                                        |
| sqlite_synth             | 1.60 us                                                     | 1.91 us: 1.20x slower                                       |
| sqlglot_normalize        | 171 ms                                                      | 205 ms: 1.20x slower                                        |
| nqueens                  | 55.5 ms                                                     | 66.6 ms: 1.20x slower                                       |
| pprint_safe_repr         | 493 ms                                                      | 592 ms: 1.20x slower                                        |
| sqlglot_optimize         | 33.1 ms                                                     | 39.8 ms: 1.20x slower                                       |
| xml_etree_process        | 36.5 ms                                                     | 44.5 ms: 1.22x slower                                       |
| docutils                 | 1.57 sec                                                    | 1.92 sec: 1.22x slower                                      |
| chameleon                | 4.72 ms                                                     | 5.79 ms: 1.23x slower                                       |
| pycparser                | 758 ms                                                      | 930 ms: 1.23x slower                                        |
| tomli_loads              | 1.36 sec                                                    | 1.67 sec: 1.23x slower                                      |
| pprint_pformat           | 991 ms                                                      | 1.22 sec: 1.23x slower                                      |
| sympy_sum                | 86.4 ms                                                     | 107 ms: 1.24x slower                                        |
| sympy_integrate          | 12.3 ms                                                     | 15.3 ms: 1.25x slower                                       |
| dulwich_log              | 40.4 ms                                                     | 50.5 ms: 1.25x slower                                       |
| genshi_xml               | 32.8 ms                                                     | 41.0 ms: 1.25x slower                                       |
| coroutines               | 12.5 ms                                                     | 16.0 ms: 1.28x slower                                       |
| float                    | 48.1 ms                                                     | 61.7 ms: 1.28x slower                                       |
| mdp                      | 1.38 sec                                                    | 1.78 sec: 1.29x slower                                      |
| asyncio_tcp_ssl          | 1.64 sec                                                    | 2.11 sec: 1.29x slower                                      |
| mypy2                    | 429 ms                                                      | 555 ms: 1.29x slower                                        |
| spectral_norm            | 59.2 ms                                                     | 77.3 ms: 1.30x slower                                       |
| deepcopy_memo            | 21.8 us                                                     | 28.8 us: 1.32x slower                                       |
| html5lib                 | 38.6 ms                                                     | 51.0 ms: 1.32x slower                                       |
| regex_compile            | 80.1 ms                                                     | 106 ms: 1.32x slower                                        |
| django_template          | 21.8 ms                                                     | 28.9 ms: 1.33x slower                                       |
| genshi_text              | 14.9 ms                                                     | 19.8 ms: 1.33x slower                                       |
| scimark_monte_carlo      | 40.3 ms                                                     | 57.3 ms: 1.42x slower                                       |
| unpickle_pure_python     | 127 us                                                      | 183 us: 1.45x slower                                        |
| mako                     | 6.24 ms                                                     | 9.03 ms: 1.45x slower                                       |
| crypto_pyaes             | 42.8 ms                                                     | 62.5 ms: 1.46x slower                                       |
| pickle_pure_python       | 183 us                                                      | 270 us: 1.47x slower                                        |
| scimark_sor              | 72.0 ms                                                     | 106 ms: 1.47x slower                                        |
| pyflate                  | 275 ms                                                      | 409 ms: 1.49x slower                                        |
| sqlglot_transpile        | 952 us                                                      | 1.48 ms: 1.55x slower                                       |
| hexiom                   | 3.69 ms                                                     | 5.74 ms: 1.56x slower                                       |
| scimark_lu               | 54.0 ms                                                     | 85.8 ms: 1.59x slower                                       |
| json_dumps               | 5.76 ms                                                     | 9.16 ms: 1.59x slower                                       |
| sqlglot_parse            | 761 us                                                      | 1.22 ms: 1.60x slower                                       |
| comprehensions           | 10.2 us                                                     | 16.5 us: 1.61x slower                                       |
| chaos                    | 37.9 ms                                                     | 61.7 ms: 1.63x slower                                       |
| richards                 | 26.0 ms                                                     | 42.4 ms: 1.63x slower                                       |
| go                       | 84.6 ms                                                     | 139 ms: 1.64x slower                                        |
| async_tree_cpu_io_mixed  | 387 ms                                                      | 638 ms: 1.65x slower                                        |
| pylint                   | 211 ms                                                      | 350 ms: 1.66x slower                                        |
| generators               | 19.5 ms                                                     | 32.4 ms: 1.66x slower                                       |
| raytrace                 | 156 ms                                                      | 273 ms: 1.75x slower                                        |
| richards_super           | 29.3 ms                                                     | 52.2 ms: 1.78x slower                                       |
| logging_silent           | 51.0 ns                                                     | 94.6 ns: 1.86x slower                                       |
| async_tree_memoization   | 271 ms                                                      | 526 ms: 1.94x slower                                        |
| async_tree_none          | 223 ms                                                      | 435 ms: 1.95x slower                                        |
| async_tree_io            | 521 ms                                                      | 1.11 sec: 2.13x slower                                      |
| deltablue                | 1.86 ms                                                     | 4.19 ms: 2.25x slower                                       |
| typing_runtime_protocols | 100 us                                                      | 336 us: 3.35x slower                                        |
| Geometric mean           | (ref)                                                       | 1.22x slower                                                |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.21x
- 99% likely to have a slowdown of 1.20x

# Memory
- memory change: unknown