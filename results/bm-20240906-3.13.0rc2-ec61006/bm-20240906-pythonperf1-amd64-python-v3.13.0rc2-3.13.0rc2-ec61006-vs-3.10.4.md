# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc2
- machine: windows-amd64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.219x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 216 ms: 1.14x faster                                              |
| chameleon      | 5.79 ms                                                     | 4.89 ms: 1.18x faster                                             |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                            |
| html5lib       | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                             |
| tornado_http   | 108 ms                                                      | 92.6 ms: 1.17x faster                                             |
| Geometric mean | (ref)                                                       | 1.18x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 222 ms: 1.96x faster                                              |
| async_tree_memoization  | 526 ms                                                      | 273 ms: 1.93x faster                                              |
| async_tree_io           | 1.11 sec                                                    | 591 ms: 1.88x faster                                              |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                              |
| Geometric mean          | (ref)                                                       | 1.85x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.1 ms: 1.23x faster                                             |
| nbody          | 71.3 ms                                                     | 68.0 ms: 1.05x faster                                             |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                       | 1.08x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.0 ms: 1.29x faster                                             |
| regex_dna      | 136 ms                                                      | 126 ms: 1.08x faster                                              |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                             |
| regex_v8       | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                       | 1.10x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.80 ms: 1.58x faster                                             |
| pickle_pure_python   | 270 us                                                      | 185 us: 1.46x faster                                              |
| unpickle_pure_python | 183 us                                                      | 126 us: 1.46x faster                                              |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                            |
| xml_etree_process    | 44.5 ms                                                     | 37.8 ms: 1.18x faster                                             |
| unpickle_list        | 2.71 us                                                     | 2.60 us: 1.04x faster                                             |
| xml_etree_parse      | 96.8 ms                                                     | 92.9 ms: 1.04x faster                                             |
| unpickle             | 9.09 us                                                     | 8.78 us: 1.04x faster                                             |
| xml_etree_generate   | 55.5 ms                                                     | 54.4 ms: 1.02x faster                                             |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                             |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                             |
| pickle               | 6.85 us                                                     | 6.91 us: 1.01x slower                                             |
| pickle_list          | 2.75 us                                                     | 2.94 us: 1.07x slower                                             |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                             |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                             |
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                             |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.50 ms: 1.39x faster                                             |
| django_template | 28.9 ms                                                     | 22.1 ms: 1.31x faster                                             |
| genshi_text     | 19.8 ms                                                     | 15.2 ms: 1.31x faster                                             |
| genshi_xml      | 41.0 ms                                                     | 32.0 ms: 1.28x faster                                             |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.23x faster                                              |
| deltablue                | 4.19 ms                                                     | 1.90 ms: 2.20x faster                                             |
| async_tree_none          | 435 ms                                                      | 222 ms: 1.96x faster                                              |
| async_tree_memoization   | 526 ms                                                      | 273 ms: 1.93x faster                                              |
| pylint                   | 350 ms                                                      | 186 ms: 1.89x faster                                              |
| async_tree_io            | 1.11 sec                                                    | 591 ms: 1.88x faster                                              |
| logging_silent           | 94.6 ns                                                     | 53.3 ns: 1.78x faster                                             |
| richards_super           | 52.2 ms                                                     | 29.5 ms: 1.77x faster                                             |
| raytrace                 | 273 ms                                                      | 162 ms: 1.69x faster                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                              |
| go                       | 139 ms                                                      | 85.7 ms: 1.62x faster                                             |
| richards                 | 42.4 ms                                                     | 26.2 ms: 1.62x faster                                             |
| chaos                    | 61.7 ms                                                     | 38.3 ms: 1.61x faster                                             |
| generators               | 32.4 ms                                                     | 20.2 ms: 1.60x faster                                             |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                             |
| json_dumps               | 9.16 ms                                                     | 5.80 ms: 1.58x faster                                             |
| hexiom                   | 5.74 ms                                                     | 3.75 ms: 1.53x faster                                             |
| sqlglot_parse            | 1.22 ms                                                     | 793 us: 1.53x faster                                              |
| scimark_lu               | 85.8 ms                                                     | 56.5 ms: 1.52x faster                                             |
| sqlglot_transpile        | 1.48 ms                                                     | 985 us: 1.50x faster                                              |
| pickle_pure_python       | 270 us                                                      | 185 us: 1.46x faster                                              |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.46x faster                                              |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                              |
| scimark_sor              | 106 ms                                                      | 75.3 ms: 1.41x faster                                             |
| crypto_pyaes             | 62.5 ms                                                     | 44.6 ms: 1.40x faster                                             |
| mako                     | 9.03 ms                                                     | 6.50 ms: 1.39x faster                                             |
| asyncio_tcp              | 732 ms                                                      | 530 ms: 1.38x faster                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.8 ms: 1.37x faster                                             |
| django_template          | 28.9 ms                                                     | 22.1 ms: 1.31x faster                                             |
| genshi_text              | 19.8 ms                                                     | 15.2 ms: 1.31x faster                                             |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.63 sec: 1.30x faster                                            |
| regex_compile            | 106 ms                                                      | 82.0 ms: 1.29x faster                                             |
| genshi_xml               | 41.0 ms                                                     | 32.0 ms: 1.28x faster                                             |
| mypy2                    | 555 ms                                                      | 433 ms: 1.28x faster                                              |
| html5lib                 | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                             |
| pycparser                | 930 ms                                                      | 733 ms: 1.27x faster                                              |
| deepcopy_memo            | 28.8 us                                                     | 22.7 us: 1.27x faster                                             |
| spectral_norm            | 77.3 ms                                                     | 61.2 ms: 1.26x faster                                             |
| coroutines               | 16.0 ms                                                     | 12.9 ms: 1.24x faster                                             |
| float                    | 61.7 ms                                                     | 50.1 ms: 1.23x faster                                             |
| sympy_sum                | 107 ms                                                      | 87.3 ms: 1.23x faster                                             |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                             |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                            |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                            |
| dulwich_log              | 50.5 ms                                                     | 42.0 ms: 1.20x faster                                             |
| sqlglot_optimize         | 39.8 ms                                                     | 33.2 ms: 1.20x faster                                             |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.20x faster                                            |
| pprint_safe_repr         | 592 ms                                                      | 494 ms: 1.20x faster                                              |
| unpack_sequence          | 39.6 ns                                                     | 33.1 ns: 1.20x faster                                             |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                             |
| chameleon                | 5.79 ms                                                     | 4.89 ms: 1.18x faster                                             |
| sqlglot_normalize        | 205 ms                                                      | 174 ms: 1.18x faster                                              |
| xml_etree_process        | 44.5 ms                                                     | 37.8 ms: 1.18x faster                                             |
| tornado_http             | 108 ms                                                      | 92.6 ms: 1.17x faster                                             |
| nqueens                  | 66.6 ms                                                     | 57.3 ms: 1.16x faster                                             |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.35 ms: 1.16x faster                                             |
| bench_thread_pool        | 958 us                                                      | 832 us: 1.15x faster                                              |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                              |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                            |
| deepcopy                 | 255 us                                                      | 223 us: 1.14x faster                                              |
| 2to3                     | 246 ms                                                      | 216 ms: 1.14x faster                                              |
| logging_format           | 6.76 us                                                     | 6.09 us: 1.11x faster                                             |
| logging_simple           | 6.22 us                                                     | 5.67 us: 1.10x faster                                             |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                             |
| scimark_fft              | 187 ms                                                      | 172 ms: 1.09x faster                                              |
| regex_dna                | 136 ms                                                      | 126 ms: 1.08x faster                                              |
| sympy_expand             | 314 ms                                                      | 291 ms: 1.08x faster                                              |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                             |
| aiohttp                  | 995 us                                                      | 946 us: 1.05x faster                                              |
| meteor_contest           | 75.9 ms                                                     | 72.2 ms: 1.05x faster                                             |
| nbody                    | 71.3 ms                                                     | 68.0 ms: 1.05x faster                                             |
| unpickle_list            | 2.71 us                                                     | 2.60 us: 1.04x faster                                             |
| xml_etree_parse          | 96.8 ms                                                     | 92.9 ms: 1.04x faster                                             |
| unpickle                 | 9.09 us                                                     | 8.78 us: 1.04x faster                                             |
| fannkuch                 | 256 ms                                                      | 248 ms: 1.03x faster                                              |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                             |
| xml_etree_generate       | 55.5 ms                                                     | 54.4 ms: 1.02x faster                                             |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                             |
| regex_v8                 | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                             |
| flaskblogging            | 2.03 sec                                                    | 2.04 sec: 1.00x slower                                            |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                             |
| pickle                   | 6.85 us                                                     | 6.91 us: 1.01x slower                                             |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                              |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                              |
| pathlib                  | 75.7 ms                                                     | 79.6 ms: 1.05x slower                                             |
| pickle_list              | 2.75 us                                                     | 2.94 us: 1.07x slower                                             |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                             |
| python_startup           | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                             |
| bench_mp_pool            | 62.0 ms                                                     | 68.0 ms: 1.10x slower                                             |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                             |
| create_gc_cycles         | 800 us                                                      | 901 us: 1.13x slower                                              |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                             |
| coverage                 | 39.0 ms                                                     | 46.0 ms: 1.18x slower                                             |
| telco                    | 3.94 ms                                                     | 4.74 ms: 1.20x slower                                             |
| thrift                   | 617 us                                                      | 8.64 ms: 13.99x slower                                            |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                      |
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.219x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown