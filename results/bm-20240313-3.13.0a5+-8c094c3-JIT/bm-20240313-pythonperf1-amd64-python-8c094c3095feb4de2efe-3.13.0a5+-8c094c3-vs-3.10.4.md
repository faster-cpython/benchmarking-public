# Results vs. 3.10.4

- fork: python
- ref: 8c094c3095feb4de2efe
- machine: windows-amd64
- commit hash: 8c094c3
- commit date: 2024-03-13
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.76 ms: 1.22x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.0 ms: 1.38x faster                                                       |
| tornado_http   | 108 ms                                                      | 85.0 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 260 ms: 1.67x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 336 ms: 1.56x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 716 ms: 1.55x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 446 ms: 1.43x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.55x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.8 ms: 1.29x faster                                                       |
| nbody          | 71.3 ms                                                     | 58.7 ms: 1.21x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.1 ms: 1.28x faster                                                       |
| regex_dna      | 136 ms                                                      | 126 ms: 1.08x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 17.3 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.49 ms: 1.67x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 178 us: 1.51x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 127 us: 1.44x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.18 sec: 1.41x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.9 ms: 1.21x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.64 us: 1.05x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.2 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.02x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.77 us: 1.01x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 17.9 us: 1.04x slower                                                       |
| pickle               | 6.85 us                                                     | 7.55 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.7 ms: 1.20x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 22.5 ms: 1.45x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.54 ms: 1.63x faster                                                       |
| django_template | 28.9 ms                                                     | 21.5 ms: 1.34x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.9 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 71.1 us: 4.72x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.03 ms: 2.06x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.5 ns: 1.71x faster                                                       |
| pylint                   | 350 ms                                                      | 209 ms: 1.67x faster                                                        |
| async_tree_none          | 435 ms                                                      | 260 ms: 1.67x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.49 ms: 1.67x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.66x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.54 ms: 1.63x faster                                                       |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.63x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 772 us: 1.57x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.4 ms: 1.57x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 336 ms: 1.56x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 470 ms: 1.56x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 716 ms: 1.55x faster                                                        |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 51.0 ms: 1.52x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 178 us: 1.51x faster                                                        |
| richards                 | 42.4 ms                                                     | 28.2 ms: 1.51x faster                                                       |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 991 us: 1.49x faster                                                        |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                                        |
| go                       | 139 ms                                                      | 96.1 ms: 1.45x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 43.3 ms: 1.44x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 127 us: 1.44x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 446 ms: 1.43x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.18 sec: 1.41x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.0 ms: 1.38x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.9 ms: 1.37x faster                                                       |
| django_template          | 28.9 ms                                                     | 21.5 ms: 1.34x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.32 ms: 1.33x faster                                                       |
| pycparser                | 930 ms                                                      | 716 ms: 1.30x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                       |
| float                    | 61.7 ms                                                     | 47.8 ms: 1.29x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 954 ms: 1.28x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.65 sec: 1.28x faster                                                      |
| regex_compile            | 106 ms                                                      | 83.1 ms: 1.28x faster                                                       |
| tornado_http             | 108 ms                                                      | 85.0 ms: 1.27x faster                                                       |
| mypy2                    | 555 ms                                                      | 436 ms: 1.27x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 39.7 ms: 1.27x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 466 ms: 1.27x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 22.8 us: 1.26x faster                                                       |
| scimark_sor              | 106 ms                                                      | 84.4 ms: 1.26x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.24x faster                                                      |
| chameleon                | 5.79 ms                                                     | 4.76 ms: 1.22x faster                                                       |
| nbody                    | 71.3 ms                                                     | 58.7 ms: 1.21x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 70.7 ms: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 88.5 ms: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.21x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.9 ms: 1.21x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                      |
| sympy_str                | 194 ms                                                      | 164 ms: 1.19x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 34.9 ms: 1.18x faster                                                       |
| fannkuch                 | 256 ms                                                      | 217 ms: 1.18x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 175 ms: 1.17x faster                                                        |
| deepcopy                 | 255 us                                                      | 219 us: 1.17x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.16x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 34.3 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.39 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 847 us: 1.13x faster                                                        |
| aiohttp                  | 995 us                                                      | 889 us: 1.12x faster                                                        |
| sympy_expand             | 314 ms                                                      | 281 ms: 1.12x faster                                                        |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 60.3 ms: 1.10x faster                                                       |
| scimark_fft              | 187 ms                                                      | 172 ms: 1.09x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.24 us: 1.08x faster                                                       |
| regex_dna                | 136 ms                                                      | 126 ms: 1.08x faster                                                        |
| create_gc_cycles         | 800 us                                                      | 745 us: 1.07x faster                                                        |
| logging_simple           | 6.22 us                                                     | 5.87 us: 1.06x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.64 us: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.2 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.02x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.0 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| pickle_list              | 2.75 us                                                     | 2.77 us: 1.01x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 76.6 ms: 1.01x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 17.9 us: 1.04x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.50 ms: 1.06x slower                                                       |
| json                     | 3.14 ms                                                     | 3.36 ms: 1.07x slower                                                       |
| async_generators         | 222 ms                                                      | 238 ms: 1.07x slower                                                        |
| pickle                   | 6.85 us                                                     | 7.55 us: 1.10x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 17.3 ms: 1.12x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 70.3 ms: 1.13x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.57 ms: 1.16x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.7 ms: 1.20x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.1 ms: 1.21x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 48.6 ns: 1.23x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 22.5 ms: 1.45x slower                                                       |
| thrift                   | 617 us                                                      | 9.00 ms: 14.58x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240313-3.13.0a5+-8c094c3-JIT/bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x


# Memory

- memory change: unknown