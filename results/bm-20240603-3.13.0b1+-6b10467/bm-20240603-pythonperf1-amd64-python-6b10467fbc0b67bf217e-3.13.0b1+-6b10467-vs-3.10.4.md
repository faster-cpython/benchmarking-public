# Results vs. 3.10.4

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: windows-amd64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 207 ms: 1.19x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.70 ms: 1.23x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                      |
| html5lib       | 51.0 ms                                                     | 35.3 ms: 1.45x faster                                                       |
| tornado_http   | 108 ms                                                      | 82.1 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 216 ms: 2.02x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 263 ms: 2.00x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 580 ms: 1.91x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 388 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.89x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.6 ms: 1.22x faster                                                       |
| nbody          | 71.3 ms                                                     | 67.2 ms: 1.06x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.0 ms: 1.38x faster                                                       |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.55 ms: 1.65x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 175 us: 1.54x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 123 us: 1.49x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.44 us: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.3 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.3 ms: 1.04x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.7 us: 1.02x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.68 us: 1.01x faster                                                       |
| pickle               | 6.85 us                                                     | 7.19 us: 1.05x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.03 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.4 ms: 1.01x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.5 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.36 ms: 1.42x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 14.7 ms: 1.34x faster                                                       |
| django_template | 28.9 ms                                                     | 21.6 ms: 1.33x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 33.1 ms: 1.24x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.31x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.89 ms: 2.22x faster                                                       |
| async_tree_none          | 435 ms                                                      | 216 ms: 2.02x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 263 ms: 2.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 580 ms: 1.91x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 52.4 ns: 1.81x faster                                                       |
| richards_super           | 52.2 ms                                                     | 29.3 ms: 1.78x faster                                                       |
| pylint                   | 350 ms                                                      | 204 ms: 1.72x faster                                                        |
| raytrace                 | 273 ms                                                      | 159 ms: 1.72x faster                                                        |
| go                       | 139 ms                                                      | 82.0 ms: 1.69x faster                                                       |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.55 ms: 1.65x faster                                                       |
| richards                 | 42.4 ms                                                     | 25.7 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 388 ms: 1.64x faster                                                        |
| chaos                    | 61.7 ms                                                     | 37.6 ms: 1.64x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.1 ms: 1.58x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 768 us: 1.58x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 3.70 ms: 1.55x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 472 ms: 1.55x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 175 us: 1.54x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 971 us: 1.52x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 123 us: 1.49x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.47x faster                                                      |
| pyflate                  | 409 ms                                                      | 279 ms: 1.46x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.4 ms: 1.45x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 35.3 ms: 1.45x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.1 ms: 1.43x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.36 ms: 1.42x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 44.6 ms: 1.40x faster                                                       |
| regex_compile            | 106 ms                                                      | 77.0 ms: 1.38x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.7 ms: 1.34x faster                                                       |
| django_template          | 28.9 ms                                                     | 21.6 ms: 1.33x faster                                                       |
| mypy2                    | 555 ms                                                      | 419 ms: 1.33x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.34 sec: 1.32x faster                                                      |
| tornado_http             | 108 ms                                                      | 82.1 ms: 1.32x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 38.5 ms: 1.31x faster                                                       |
| pycparser                | 930 ms                                                      | 711 ms: 1.31x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 22.3 us: 1.29x faster                                                       |
| sympy_sum                | 107 ms                                                      | 84.6 ms: 1.27x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.25x faster                                                       |
| coroutines               | 16.0 ms                                                     | 12.8 ms: 1.25x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 33.1 ms: 1.24x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.4 ms: 1.24x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 987 ms: 1.24x faster                                                        |
| chameleon                | 5.79 ms                                                     | 4.70 ms: 1.23x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 483 ms: 1.23x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                      |
| float                    | 61.7 ms                                                     | 50.6 ms: 1.22x faster                                                       |
| sympy_str                | 194 ms                                                      | 161 ms: 1.21x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 794 us: 1.21x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 33.0 ms: 1.21x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                      |
| 2to3                     | 246 ms                                                      | 207 ms: 1.19x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 174 ms: 1.18x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 56.7 ms: 1.18x faster                                                       |
| deepcopy                 | 255 us                                                      | 218 us: 1.17x faster                                                        |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.39 ms: 1.14x faster                                                       |
| sympy_expand             | 314 ms                                                      | 276 ms: 1.14x faster                                                        |
| scimark_fft              | 187 ms                                                      | 167 ms: 1.12x faster                                                        |
| aiohttp                  | 995 us                                                      | 891 us: 1.12x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.98 us: 1.12x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.13 us: 1.10x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.71 us: 1.09x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.44 us: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.3 ms: 1.06x faster                                                       |
| nbody                    | 71.3 ms                                                     | 67.2 ms: 1.06x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.0 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.3 ms: 1.04x faster                                                       |
| fannkuch                 | 256 ms                                                      | 250 ms: 1.02x faster                                                        |
| json_loads               | 14.0 us                                                     | 13.7 us: 1.02x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 74.8 ms: 1.01x faster                                                       |
| python_startup           | 20.6 ms                                                     | 20.4 ms: 1.01x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.68 us: 1.01x faster                                                       |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| async_generators         | 222 ms                                                      | 223 ms: 1.01x slower                                                        |
| bench_mp_pool            | 62.0 ms                                                     | 65.1 ms: 1.05x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.19 us: 1.05x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.5 ms: 1.07x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.03 us: 1.10x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                       |
| coverage                 | 39.0 ms                                                     | 43.2 ms: 1.11x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 906 us: 1.13x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.60 ms: 1.17x slower                                                       |
| thrift                   | 617 us                                                      | 8.10 ms: 13.12x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                |
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240603-3.13.0b1+-6b10467/bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown