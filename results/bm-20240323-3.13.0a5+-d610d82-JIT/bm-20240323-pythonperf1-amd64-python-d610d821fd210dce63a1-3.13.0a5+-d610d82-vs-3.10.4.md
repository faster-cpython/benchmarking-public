# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-amd64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.58 ms: 1.26x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 35.8 ms: 1.43x faster                                                       |
| tornado_http   | 108 ms                                                      | 85.1 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 222 ms: 1.96x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 275 ms: 1.92x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 586 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.85x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.2 ms: 1.34x faster                                                       |
| nbody          | 71.3 ms                                                     | 57.0 ms: 1.25x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.7 ms: 1.27x faster                                                       |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 173 us: 1.56x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 126 us: 1.45x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.20 sec: 1.39x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 52.6 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.67 us: 1.05x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.02x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 17.4 us: 1.01x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.78 us: 1.02x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.87 us: 1.04x slower                                                       |
| pickle               | 6.85 us                                                     | 7.36 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.2 ms: 1.12x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.8 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.71 ms: 1.58x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                       |
| django_template | 28.9 ms                                                     | 23.2 ms: 1.25x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 69.9 us: 4.80x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.08 ms: 2.02x faster                                                       |
| async_tree_none          | 435 ms                                                      | 222 ms: 1.96x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 275 ms: 1.92x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 586 ms: 1.89x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 54.8 ns: 1.73x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.5 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                                       |
| pylint                   | 350 ms                                                      | 215 ms: 1.63x faster                                                        |
| generators               | 32.4 ms                                                     | 20.4 ms: 1.59x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.71 ms: 1.58x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 464 ms: 1.58x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 173 us: 1.56x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 783 us: 1.55x faster                                                        |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 50.9 ms: 1.52x faster                                                       |
| richards                 | 42.4 ms                                                     | 28.0 ms: 1.51x faster                                                       |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                        |
| go                       | 139 ms                                                      | 92.6 ms: 1.50x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.00 ms: 1.47x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.45x faster                                                        |
| pyflate                  | 409 ms                                                      | 283 ms: 1.45x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 43.3 ms: 1.44x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 35.8 ms: 1.43x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.20 sec: 1.39x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.3 ms: 1.39x faster                                                       |
| pycparser                | 930 ms                                                      | 676 ms: 1.38x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 21.2 us: 1.36x faster                                                       |
| float                    | 61.7 ms                                                     | 46.2 ms: 1.34x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.37 ms: 1.32x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                       |
| scimark_sor              | 106 ms                                                      | 81.3 ms: 1.31x faster                                                       |
| tornado_http             | 108 ms                                                      | 85.1 ms: 1.27x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.67 sec: 1.27x faster                                                      |
| regex_compile            | 106 ms                                                      | 83.7 ms: 1.27x faster                                                       |
| chameleon                | 5.79 ms                                                     | 4.58 ms: 1.26x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 975 ms: 1.25x faster                                                        |
| nbody                    | 71.3 ms                                                     | 57.0 ms: 1.25x faster                                                       |
| django_template          | 28.9 ms                                                     | 23.2 ms: 1.25x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.6 ms: 1.24x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 476 ms: 1.24x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.23 ms: 1.22x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 70.4 ms: 1.22x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.9 ms: 1.22x faster                                                       |
| mypy2                    | 555 ms                                                      | 462 ms: 1.20x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                       |
| sympy_str                | 194 ms                                                      | 165 ms: 1.18x faster                                                        |
| deepcopy                 | 255 us                                                      | 219 us: 1.16x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                       |
| fannkuch                 | 256 ms                                                      | 222 ms: 1.15x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 837 us: 1.14x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 183 ms: 1.12x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 35.4 ms: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| sympy_expand             | 314 ms                                                      | 284 ms: 1.11x faster                                                        |
| scimark_fft              | 187 ms                                                      | 169 ms: 1.11x faster                                                        |
| aiohttp                  | 995 us                                                      | 899 us: 1.11x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 60.7 ms: 1.10x faster                                                       |
| create_gc_cycles         | 800 us                                                      | 733 us: 1.09x faster                                                        |
| json                     | 3.14 ms                                                     | 2.90 ms: 1.08x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.39 us: 1.06x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.6 ms: 1.06x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.67 us: 1.05x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.96 us: 1.04x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.2 ms: 1.02x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.02x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| pickle_dict              | 17.2 us                                                     | 17.4 us: 1.01x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 76.9 ms: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.78 us: 1.02x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.87 us: 1.04x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.48 ms: 1.05x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.36 us: 1.08x slower                                                       |
| async_generators         | 222 ms                                                      | 244 ms: 1.10x slower                                                        |
| bench_mp_pool            | 62.0 ms                                                     | 68.7 ms: 1.11x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.2 ms: 1.12x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.4 ms: 1.19x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 47.7 ns: 1.20x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.77 ms: 1.21x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.8 ms: 1.34x slower                                                       |
| thrift                   | 617 us                                                      | 8.86 ms: 14.35x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                |
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x


# Memory

- memory change: unknown