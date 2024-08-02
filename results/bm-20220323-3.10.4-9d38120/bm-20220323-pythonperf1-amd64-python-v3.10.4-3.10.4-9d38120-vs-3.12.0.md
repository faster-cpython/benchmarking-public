
# Results vs. 3.12.0

- fork: python
- ref: v3.10.4
- machine: windows-amd64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.19x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 246 ms: 1.13x slower                                        |
| chameleon      | 4.98 ms                                                     | 5.79 ms: 1.16x slower                                       |
| docutils       | 1.66 sec                                                    | 1.92 sec: 1.16x slower                                      |
| tornado_http   | 89.5 ms                                                     | 108 ms: 1.21x slower                                        |
| Geometric mean | (ref)                                                       | 1.16x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_cpu_io_mixed | 489 ms                                                      | 638 ms: 1.30x slower                                        |
| async_tree_none         | 291 ms                                                      | 435 ms: 1.49x slower                                        |
| async_tree_io           | 731 ms                                                      | 1.11 sec: 1.52x slower                                      |
| async_tree_memoization  | 339 ms                                                      | 526 ms: 1.55x slower                                        |
| Geometric mean          | (ref)                                                       | 1.46x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                        |
| nbody          | 71.9 ms                                                     | 71.3 ms: 1.01x faster                                       |
| float          | 56.8 ms                                                     | 61.7 ms: 1.09x slower                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.66 ms: 1.02x slower                                       |
| regex_dna      | 126 ms                                                      | 136 ms: 1.08x slower                                        |
| regex_v8       | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                       |
| regex_compile  | 87.5 ms                                                     | 106 ms: 1.21x slower                                        |
| Geometric mean | (ref)                                                       | 1.10x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 6.85 us: 1.09x faster                                       |
| pickle_dict          | 18.4 us                                                     | 17.2 us: 1.07x faster                                       |
| pickle_list          | 2.83 us                                                     | 2.75 us: 1.03x faster                                       |
| unpickle_list        | 2.75 us                                                     | 2.71 us: 1.01x faster                                       |
| xml_etree_generate   | 55.8 ms                                                     | 55.5 ms: 1.01x faster                                       |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                       |
| xml_etree_parse      | 93.0 ms                                                     | 96.8 ms: 1.04x slower                                       |
| unpickle             | 8.18 us                                                     | 9.09 us: 1.11x slower                                       |
| xml_etree_process    | 37.7 ms                                                     | 44.5 ms: 1.18x slower                                       |
| tomli_loads          | 1.37 sec                                                    | 1.67 sec: 1.22x slower                                      |
| unpickle_pure_python | 133 us                                                      | 183 us: 1.38x slower                                        |
| pickle_pure_python   | 195 us                                                      | 270 us: 1.38x slower                                        |
| json_dumps           | 5.70 ms                                                     | 9.16 ms: 1.61x slower                                       |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 15.5 ms: 1.05x faster                                       |
| python_startup         | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 28.9 ms: 1.26x slower                                       |
| mako            | 7.09 ms                                                     | 9.03 ms: 1.27x slower                                       |
| Geometric mean  | (ref)                                                       | 1.27x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| bench_mp_pool            | 69.2 ms                                                     | 62.0 ms: 1.11x faster                                       |
| pickle                   | 7.43 us                                                     | 6.85 us: 1.09x faster                                       |
| async_generators         | 239 ms                                                      | 222 ms: 1.08x faster                                        |
| gc_traversal             | 1.52 ms                                                     | 1.41 ms: 1.08x faster                                       |
| pickle_dict              | 18.4 us                                                     | 17.2 us: 1.07x faster                                       |
| pathlib                  | 80.5 ms                                                     | 75.7 ms: 1.06x faster                                       |
| telco                    | 4.13 ms                                                     | 3.94 ms: 1.05x faster                                       |
| python_startup_no_site   | 16.2 ms                                                     | 15.5 ms: 1.05x faster                                       |
| coverage                 | 40.8 ms                                                     | 39.0 ms: 1.05x faster                                       |
| pickle_list              | 2.83 us                                                     | 2.75 us: 1.03x faster                                       |
| pidigits                 | 152 ms                                                      | 149 ms: 1.02x faster                                        |
| unpickle_list            | 2.75 us                                                     | 2.71 us: 1.01x faster                                       |
| logging_simple           | 6.28 us                                                     | 6.22 us: 1.01x faster                                       |
| nbody                    | 71.9 ms                                                     | 71.3 ms: 1.01x faster                                       |
| xml_etree_generate       | 55.8 ms                                                     | 55.5 ms: 1.01x faster                                       |
| logging_format           | 6.72 us                                                     | 6.76 us: 1.01x slower                                       |
| json_loads               | 13.9 us                                                     | 14.0 us: 1.01x slower                                       |
| scimark_fft              | 184 ms                                                      | 187 ms: 1.02x slower                                        |
| meteor_contest           | 74.6 ms                                                     | 75.9 ms: 1.02x slower                                       |
| regex_effbot             | 1.62 ms                                                     | 1.66 ms: 1.02x slower                                       |
| json                     | 3.05 ms                                                     | 3.14 ms: 1.03x slower                                       |
| fannkuch                 | 247 ms                                                      | 256 ms: 1.04x slower                                        |
| xml_etree_parse          | 93.0 ms                                                     | 96.8 ms: 1.04x slower                                       |
| deepcopy_reduce          | 2.09 us                                                     | 2.20 us: 1.05x slower                                       |
| unpack_sequence          | 37.5 ns                                                     | 39.6 ns: 1.06x slower                                       |
| python_startup           | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                       |
| nqueens                  | 62.8 ms                                                     | 66.6 ms: 1.06x slower                                       |
| create_gc_cycles         | 752 us                                                      | 800 us: 1.06x slower                                        |
| scimark_sparse_mat_mult  | 2.56 ms                                                     | 2.72 ms: 1.07x slower                                       |
| deepcopy                 | 238 us                                                      | 255 us: 1.07x slower                                        |
| regex_dna                | 126 ms                                                      | 136 ms: 1.08x slower                                        |
| regex_v8                 | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                       |
| sqlite_synth             | 1.76 us                                                     | 1.91 us: 1.09x slower                                       |
| float                    | 56.8 ms                                                     | 61.7 ms: 1.09x slower                                       |
| mypy2                    | 509 ms                                                      | 555 ms: 1.09x slower                                        |
| sqlglot_normalize        | 187 ms                                                      | 205 ms: 1.10x slower                                        |
| sympy_expand             | 284 ms                                                      | 314 ms: 1.11x slower                                        |
| sympy_str                | 175 ms                                                      | 194 ms: 1.11x slower                                        |
| unpickle                 | 8.18 us                                                     | 9.09 us: 1.11x slower                                       |
| bench_thread_pool        | 857 us                                                      | 958 us: 1.12x slower                                        |
| coroutines               | 14.3 ms                                                     | 16.0 ms: 1.12x slower                                       |
| aiohttp                  | 884 us                                                      | 995 us: 1.13x slower                                        |
| 2to3                     | 218 ms                                                      | 246 ms: 1.13x slower                                        |
| dulwich_log              | 44.3 ms                                                     | 50.5 ms: 1.14x slower                                       |
| sqlglot_optimize         | 34.5 ms                                                     | 39.8 ms: 1.15x slower                                       |
| pprint_safe_repr         | 513 ms                                                      | 592 ms: 1.15x slower                                        |
| spectral_norm            | 66.9 ms                                                     | 77.3 ms: 1.15x slower                                       |
| docutils                 | 1.66 sec                                                    | 1.92 sec: 1.16x slower                                      |
| chameleon                | 4.98 ms                                                     | 5.79 ms: 1.16x slower                                       |
| pprint_pformat           | 1.05 sec                                                    | 1.22 sec: 1.17x slower                                      |
| comprehensions           | 14.1 us                                                     | 16.5 us: 1.17x slower                                       |
| sympy_sum                | 91.5 ms                                                     | 107 ms: 1.17x slower                                        |
| xml_etree_process        | 37.7 ms                                                     | 44.5 ms: 1.18x slower                                       |
| sympy_integrate          | 13.0 ms                                                     | 15.3 ms: 1.18x slower                                       |
| dask                     | 263 ms                                                      | 313 ms: 1.19x slower                                        |
| sqlalchemy_declarative   | 86.4 ms                                                     | 103 ms: 1.20x slower                                        |
| tornado_http             | 89.5 ms                                                     | 108 ms: 1.21x slower                                        |
| regex_compile            | 87.5 ms                                                     | 106 ms: 1.21x slower                                        |
| deepcopy_memo            | 23.7 us                                                     | 28.8 us: 1.21x slower                                       |
| tomli_loads              | 1.37 sec                                                    | 1.67 sec: 1.22x slower                                      |
| sqlalchemy_imperative    | 9.29 ms                                                     | 11.4 ms: 1.23x slower                                       |
| django_template          | 22.9 ms                                                     | 28.9 ms: 1.26x slower                                       |
| mako                     | 7.09 ms                                                     | 9.03 ms: 1.27x slower                                       |
| crypto_pyaes             | 48.5 ms                                                     | 62.5 ms: 1.29x slower                                       |
| mdp                      | 1.37 sec                                                    | 1.78 sec: 1.30x slower                                      |
| async_tree_cpu_io_mixed  | 489 ms                                                      | 638 ms: 1.30x slower                                        |
| scimark_monte_carlo      | 43.7 ms                                                     | 57.3 ms: 1.31x slower                                       |
| pycparser                | 699 ms                                                      | 930 ms: 1.33x slower                                        |
| scimark_sor              | 78.8 ms                                                     | 106 ms: 1.35x slower                                        |
| unpickle_pure_python     | 133 us                                                      | 183 us: 1.38x slower                                        |
| pickle_pure_python       | 195 us                                                      | 270 us: 1.38x slower                                        |
| pyflate                  | 295 ms                                                      | 409 ms: 1.39x slower                                        |
| hexiom                   | 4.10 ms                                                     | 5.74 ms: 1.40x slower                                       |
| raytrace                 | 192 ms                                                      | 273 ms: 1.42x slower                                        |
| chaos                    | 43.3 ms                                                     | 61.7 ms: 1.42x slower                                       |
| generators               | 22.5 ms                                                     | 32.4 ms: 1.44x slower                                       |
| sqlglot_transpile        | 1.02 ms                                                     | 1.48 ms: 1.44x slower                                       |
| scimark_lu               | 58.9 ms                                                     | 85.8 ms: 1.46x slower                                       |
| async_tree_none          | 291 ms                                                      | 435 ms: 1.49x slower                                        |
| richards                 | 28.4 ms                                                     | 42.4 ms: 1.50x slower                                       |
| asyncio_tcp              | 487 ms                                                      | 732 ms: 1.50x slower                                        |
| sqlglot_parse            | 804 us                                                      | 1.22 ms: 1.51x slower                                       |
| async_tree_io            | 731 ms                                                      | 1.11 sec: 1.52x slower                                      |
| go                       | 91.6 ms                                                     | 139 ms: 1.52x slower                                        |
| async_tree_memoization   | 339 ms                                                      | 526 ms: 1.55x slower                                        |
| logging_silent           | 60.5 ns                                                     | 94.6 ns: 1.56x slower                                       |
| json_dumps               | 5.70 ms                                                     | 9.16 ms: 1.61x slower                                       |
| richards_super           | 32.1 ms                                                     | 52.2 ms: 1.63x slower                                       |
| deltablue                | 2.16 ms                                                     | 4.19 ms: 1.94x slower                                       |
| typing_runtime_protocols | 95.1 us                                                     | 336 us: 3.53x slower                                        |
| Geometric mean           | (ref)                                                       | 1.19x slower                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, asyncio_tcp_ssl
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x


# Memory

- memory change: unknown