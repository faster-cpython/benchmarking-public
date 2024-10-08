# Results vs. 3.12.0

- fork: python
- ref: 93156880efd14ad7adc7
- machine: windows-amd64
- commit hash: 9315688
- commit date: 2024-07-03
- overall geometric mean: 1.00x slower
- HPT reliability: 98.32%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 91.1 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 245 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 196 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 532 ms: 1.45x faster                                                       |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                       |
| async_tree_io              | 731 ms                                                      | 545 ms: 1.34x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 80.3 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 85.8 ms: 1.02x faster                                                      |
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 17.4 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.1 ms: 1.06x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.09 ms: 1.07x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.12x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.52 ms: 1.06x slower                                                      |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 245 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 196 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 532 ms: 1.45x faster                                                       |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                       |
| async_tree_io              | 731 ms                                                      | 545 ms: 1.34x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| deepcopy                   | 238 us                                                      | 182 us: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.62 sec: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 21.0 us: 1.13x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.13x faster                                                      |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 827 us: 1.04x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 88.7 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 67.8 ms: 1.02x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 85.8 ms: 1.02x faster                                                      |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.8 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.31 us: 1.00x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.75 us: 1.00x slower                                                      |
| chaos                      | 43.3 ms                                                     | 43.6 ms: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 13.0 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 188 ms: 1.01x slower                                                       |
| pathlib                    | 80.5 ms                                                     | 81.2 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 91.1 ms: 1.02x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 68.2 ms: 1.02x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.2 ms: 1.02x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 61.8 ns: 1.02x slower                                                      |
| go                         | 91.6 ms                                                     | 93.5 ms: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.0 ms: 1.03x slower                                                      |
| sympy_expand               | 284 ms                                                      | 293 ms: 1.03x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.4 ms: 1.04x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                     |
| richards                   | 28.4 ms                                                     | 29.6 ms: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.30 ms: 1.05x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 543 ms: 1.06x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 59.1 ms: 1.06x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                     |
| mako                       | 7.09 ms                                                     | 7.52 ms: 1.06x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 51.5 ms: 1.06x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pyflate                    | 295 ms                                                      | 315 ms: 1.07x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.09 ms: 1.07x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 84.4 ms: 1.07x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 533 ms: 1.09x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 891 us: 1.11x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.4 ms: 1.11x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 65.6 ms: 1.12x slower                                                      |
| nbody                      | 71.9 ms                                                     | 80.3 ms: 1.12x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.12x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.14x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| scimark_fft                | 184 ms                                                      | 213 ms: 1.16x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.98 ms: 1.16x slower                                                      |
| fannkuch                   | 247 ms                                                      | 291 ms: 1.18x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.2 ms: 1.18x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.97 ms: 1.20x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 911 us: 1.21x slower                                                       |
| pycparser                  | 699 ms                                                      | 848 ms: 1.21x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 17.4 ms: 1.22x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (6): generators, xml_etree_parse, float, regex_effbot, json, deltablue
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240703-3.14.0a0-9315688/bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.32% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown