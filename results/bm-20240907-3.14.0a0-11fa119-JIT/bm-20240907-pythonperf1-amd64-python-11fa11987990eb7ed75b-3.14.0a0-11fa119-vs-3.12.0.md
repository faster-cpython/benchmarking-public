# Results vs. 3.12.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.04x faster
- HPT reliability: 93.96%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 241 ms: 1.10x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.91 sec: 1.15x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 97.7 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 195 ms: 1.46x faster                                                       |
| async_tree_none            | 291 ms                                                      | 201 ms: 1.45x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 555 ms: 1.39x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 393 ms: 1.28x faster                                                       |
| async_tree_io              | 731 ms                                                      | 584 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 393 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.0 ms: 1.47x faster                                                      |
| float          | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 95.2 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 49.0 ms: 1.14x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.24 sec: 1.10x faster                                                     |
| xml_etree_process    | 37.7 ms                                                     | 34.7 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.7 us: 1.04x faster                                                      |
| pickle               | 7.43 us                                                     | 7.17 us: 1.04x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 194 us: 1.01x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.86 ms: 1.03x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 141 us: 1.06x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.18 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.15 ms: 1.37x faster                                                      |
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.2 us: 1.56x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 45.6 ms: 1.47x faster                                                      |
| nbody                      | 71.9 ms                                                     | 49.0 ms: 1.47x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 195 ms: 1.46x faster                                                       |
| async_tree_none            | 291 ms                                                      | 201 ms: 1.45x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 555 ms: 1.39x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.15 ms: 1.37x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.34x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 59.9 ms: 1.32x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.31x faster                                                       |
| float                      | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.62 sec: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 393 ms: 1.28x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 38.3 ms: 1.27x faster                                                      |
| async_tree_io              | 731 ms                                                      | 584 ms: 1.25x faster                                                       |
| scimark_fft                | 184 ms                                                      | 148 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 393 ms: 1.24x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.12 ms: 1.20x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.83 ms: 1.18x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 49.0 ms: 1.14x faster                                                      |
| pyflate                    | 295 ms                                                      | 261 ms: 1.13x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 52.3 ms: 1.13x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.10x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.24 sec: 1.10x faster                                                     |
| xml_etree_process          | 37.7 ms                                                     | 34.7 ms: 1.09x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.6 ms: 1.07x faster                                                      |
| fannkuch                   | 247 ms                                                      | 232 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.3 ns: 1.06x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.97 us: 1.05x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.43 us: 1.04x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 822 us: 1.04x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.1 ms: 1.04x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.7 us: 1.04x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.5 ms: 1.04x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.17 us: 1.04x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.04x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.0 ms: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                                      |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 503 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.03 sec: 1.01x faster                                                     |
| pathlib                    | 80.5 ms                                                     | 79.5 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 194 us: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.1 ms: 1.01x slower                                                      |
| pycparser                  | 699 ms                                                      | 706 ms: 1.01x slower                                                       |
| generators                 | 22.5 ms                                                     | 22.8 ms: 1.01x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| raytrace                   | 192 ms                                                      | 196 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.86 ms: 1.03x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 71.6 ms: 1.04x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 141 us: 1.06x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 97.8 ms: 1.07x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 200 ms: 1.07x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 523 ms: 1.07x slower                                                       |
| sympy_str                  | 175 ms                                                      | 188 ms: 1.07x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 95.2 ms: 1.09x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                     |
| tornado_http               | 89.5 ms                                                     | 97.7 ms: 1.09x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 883 us: 1.10x slower                                                       |
| async_generators           | 239 ms                                                      | 264 ms: 1.10x slower                                                       |
| 2to3                       | 218 ms                                                      | 241 ms: 1.10x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.18 us: 1.12x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.15 ms: 1.12x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.64 ms: 1.12x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.8 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.14x slower                                                       |
| python_startup             | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.91 sec: 1.15x slower                                                     |
| sqlglot_optimize           | 34.5 ms                                                     | 39.8 ms: 1.15x slower                                                      |
| sympy_expand               | 284 ms                                                      | 329 ms: 1.16x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.2 ms: 1.18x slower                                                      |
| richards_super             | 32.1 ms                                                     | 38.4 ms: 1.20x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.92 ms: 1.20x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 914 us: 1.22x slower                                                       |
| richards                   | 28.4 ms                                                     | 35.8 ms: 1.26x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 58.4 ns: 1.56x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (4): xml_etree_parse, go, regex_effbot, pickle_list
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 93.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown