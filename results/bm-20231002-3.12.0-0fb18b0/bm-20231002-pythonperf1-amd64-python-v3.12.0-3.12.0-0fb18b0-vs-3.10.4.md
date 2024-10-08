
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0
- machine: windows-amd64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                        |
| chameleon      | 5.79 ms                                                     | 4.98 ms: 1.16x faster                                       |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                      |
| tornado_http   | 108 ms                                                      | 89.5 ms: 1.21x faster                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 339 ms: 1.55x faster                                        |
| async_tree_io           | 1.11 sec                                                    | 731 ms: 1.52x faster                                        |
| async_tree_none         | 435 ms                                                      | 291 ms: 1.49x faster                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 489 ms: 1.30x faster                                        |
| Geometric mean          | (ref)                                                       | 1.46x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.8 ms: 1.09x faster                                       |
| nbody          | 71.3 ms                                                     | 71.9 ms: 1.01x slower                                       |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.5 ms: 1.21x faster                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                       |
| regex_dna      | 136 ms                                                      | 126 ms: 1.08x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.70 ms: 1.61x faster                                       |
| pickle_pure_python   | 270 us                                                      | 195 us: 1.38x faster                                        |
| unpickle_pure_python | 183 us                                                      | 133 us: 1.38x faster                                        |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| xml_etree_process    | 44.5 ms                                                     | 37.7 ms: 1.18x faster                                       |
| unpickle             | 9.09 us                                                     | 8.18 us: 1.11x faster                                       |
| xml_etree_parse      | 96.8 ms                                                     | 93.0 ms: 1.04x faster                                       |
| json_loads           | 14.0 us                                                     | 13.9 us: 1.01x faster                                       |
| xml_etree_generate   | 55.5 ms                                                     | 55.8 ms: 1.01x slower                                       |
| unpickle_list        | 2.71 us                                                     | 2.75 us: 1.01x slower                                       |
| pickle_list          | 2.75 us                                                     | 2.83 us: 1.03x slower                                       |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                       |
| pickle               | 6.85 us                                                     | 7.43 us: 1.09x slower                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 19.5 ms: 1.06x faster                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.2 ms: 1.05x slower                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.09 ms: 1.27x faster                                       |
| django_template | 28.9 ms                                                     | 22.9 ms: 1.26x faster                                       |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 95.1 us: 3.53x faster                                       |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.94x faster                                       |
| richards_super           | 52.2 ms                                                     | 32.1 ms: 1.63x faster                                       |
| json_dumps               | 9.16 ms                                                     | 5.70 ms: 1.61x faster                                       |
| logging_silent           | 94.6 ns                                                     | 60.5 ns: 1.56x faster                                       |
| async_tree_memoization   | 526 ms                                                      | 339 ms: 1.55x faster                                        |
| go                       | 139 ms                                                      | 91.6 ms: 1.52x faster                                       |
| async_tree_io            | 1.11 sec                                                    | 731 ms: 1.52x faster                                        |
| sqlglot_parse            | 1.22 ms                                                     | 804 us: 1.51x faster                                        |
| asyncio_tcp              | 732 ms                                                      | 487 ms: 1.50x faster                                        |
| richards                 | 42.4 ms                                                     | 28.4 ms: 1.50x faster                                       |
| async_tree_none          | 435 ms                                                      | 291 ms: 1.49x faster                                        |
| scimark_lu               | 85.8 ms                                                     | 58.9 ms: 1.46x faster                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.02 ms: 1.44x faster                                       |
| generators               | 32.4 ms                                                     | 22.5 ms: 1.44x faster                                       |
| chaos                    | 61.7 ms                                                     | 43.3 ms: 1.42x faster                                       |
| raytrace                 | 273 ms                                                      | 192 ms: 1.42x faster                                        |
| hexiom                   | 5.74 ms                                                     | 4.10 ms: 1.40x faster                                       |
| pyflate                  | 409 ms                                                      | 295 ms: 1.39x faster                                        |
| pickle_pure_python       | 270 us                                                      | 195 us: 1.38x faster                                        |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.38x faster                                        |
| scimark_sor              | 106 ms                                                      | 78.8 ms: 1.35x faster                                       |
| pycparser                | 930 ms                                                      | 699 ms: 1.33x faster                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.7 ms: 1.31x faster                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 489 ms: 1.30x faster                                        |
| mdp                      | 1.78 sec                                                    | 1.37 sec: 1.30x faster                                      |
| crypto_pyaes             | 62.5 ms                                                     | 48.5 ms: 1.29x faster                                       |
| mako                     | 9.03 ms                                                     | 7.09 ms: 1.27x faster                                       |
| django_template          | 28.9 ms                                                     | 22.9 ms: 1.26x faster                                       |
| sqlalchemy_imperative    | 11.4 ms                                                     | 9.29 ms: 1.23x faster                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| deepcopy_memo            | 28.8 us                                                     | 23.7 us: 1.21x faster                                       |
| regex_compile            | 106 ms                                                      | 87.5 ms: 1.21x faster                                       |
| tornado_http             | 108 ms                                                      | 89.5 ms: 1.21x faster                                       |
| sqlalchemy_declarative   | 103 ms                                                      | 86.4 ms: 1.20x faster                                       |
| dask                     | 313 ms                                                      | 263 ms: 1.19x faster                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.18x faster                                       |
| xml_etree_process        | 44.5 ms                                                     | 37.7 ms: 1.18x faster                                       |
| sympy_sum                | 107 ms                                                      | 91.5 ms: 1.17x faster                                       |
| comprehensions           | 16.5 us                                                     | 14.1 us: 1.17x faster                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.05 sec: 1.17x faster                                      |
| chameleon                | 5.79 ms                                                     | 4.98 ms: 1.16x faster                                       |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                      |
| spectral_norm            | 77.3 ms                                                     | 66.9 ms: 1.15x faster                                       |
| pprint_safe_repr         | 592 ms                                                      | 513 ms: 1.15x faster                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 34.5 ms: 1.15x faster                                       |
| dulwich_log              | 50.5 ms                                                     | 44.3 ms: 1.14x faster                                       |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                        |
| aiohttp                  | 995 us                                                      | 884 us: 1.13x faster                                        |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                       |
| bench_thread_pool        | 958 us                                                      | 857 us: 1.12x faster                                        |
| unpickle                 | 9.09 us                                                     | 8.18 us: 1.11x faster                                       |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                        |
| sympy_expand             | 314 ms                                                      | 284 ms: 1.11x faster                                        |
| sqlglot_normalize        | 205 ms                                                      | 187 ms: 1.10x faster                                        |
| mypy2                    | 555 ms                                                      | 509 ms: 1.09x faster                                        |
| float                    | 61.7 ms                                                     | 56.8 ms: 1.09x faster                                       |
| sqlite_synth             | 1.91 us                                                     | 1.76 us: 1.09x faster                                       |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                       |
| regex_dna                | 136 ms                                                      | 126 ms: 1.08x faster                                        |
| deepcopy                 | 255 us                                                      | 238 us: 1.07x faster                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.56 ms: 1.07x faster                                       |
| create_gc_cycles         | 800 us                                                      | 752 us: 1.06x faster                                        |
| nqueens                  | 66.6 ms                                                     | 62.8 ms: 1.06x faster                                       |
| python_startup           | 20.6 ms                                                     | 19.5 ms: 1.06x faster                                       |
| unpack_sequence          | 39.6 ns                                                     | 37.5 ns: 1.06x faster                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.09 us: 1.05x faster                                       |
| xml_etree_parse          | 96.8 ms                                                     | 93.0 ms: 1.04x faster                                       |
| fannkuch                 | 256 ms                                                      | 247 ms: 1.04x faster                                        |
| json                     | 3.14 ms                                                     | 3.05 ms: 1.03x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                       |
| meteor_contest           | 75.9 ms                                                     | 74.6 ms: 1.02x faster                                       |
| scimark_fft              | 187 ms                                                      | 184 ms: 1.02x faster                                        |
| json_loads               | 14.0 us                                                     | 13.9 us: 1.01x faster                                       |
| logging_format           | 6.76 us                                                     | 6.72 us: 1.01x faster                                       |
| xml_etree_generate       | 55.5 ms                                                     | 55.8 ms: 1.01x slower                                       |
| nbody                    | 71.3 ms                                                     | 71.9 ms: 1.01x slower                                       |
| logging_simple           | 6.22 us                                                     | 6.28 us: 1.01x slower                                       |
| unpickle_list            | 2.71 us                                                     | 2.75 us: 1.01x slower                                       |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                        |
| pickle_list              | 2.75 us                                                     | 2.83 us: 1.03x slower                                       |
| coverage                 | 39.0 ms                                                     | 40.8 ms: 1.05x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.2 ms: 1.05x slower                                       |
| telco                    | 3.94 ms                                                     | 4.13 ms: 1.05x slower                                       |
| pathlib                  | 75.7 ms                                                     | 80.5 ms: 1.06x slower                                       |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                       |
| gc_traversal             | 1.41 ms                                                     | 1.52 ms: 1.08x slower                                       |
| async_generators         | 222 ms                                                      | 239 ms: 1.08x slower                                        |
| pickle                   | 6.85 us                                                     | 7.43 us: 1.09x slower                                       |
| bench_mp_pool            | 62.0 ms                                                     | 69.2 ms: 1.11x slower                                       |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, xml_etree_iterparse
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x


# Memory

- memory change: unknown