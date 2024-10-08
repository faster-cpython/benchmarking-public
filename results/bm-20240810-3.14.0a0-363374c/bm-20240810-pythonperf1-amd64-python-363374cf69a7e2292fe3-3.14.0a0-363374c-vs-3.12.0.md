# Results vs. 3.12.0

- fork: python
- ref: 363374cf69a7e2292fe3
- machine: windows-amd64
- commit hash: 363374c
- commit date: 2024-08-10
- overall geometric mean: 1.02x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 233 ms: 1.07x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 94.9 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 248 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 198 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 550 ms: 1.40x faster                                                       |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.33x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 266 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 398 ms: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 588 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.33x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.5 ms: 1.02x faster                                                      |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 84.9 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 92.3 ms: 1.06x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 95.4 ms: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.0 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 69.7 ms: 1.07x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 215 us: 1.10x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.7 ms: 1.11x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.34 ms: 1.11x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.9 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.85 ms: 1.03x faster                                                      |
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 248 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 198 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 550 ms: 1.40x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.55 sec: 1.35x faster                                                     |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.33x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 266 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 398 ms: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 588 ms: 1.24x faster                                                       |
| deepcopy                   | 238 us                                                      | 191 us: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 21.1 us: 1.12x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.96 us: 1.07x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.4 ms: 1.05x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 814 us: 1.05x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.85 ms: 1.03x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.9 ms: 1.03x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.2 ms: 1.03x faster                                                      |
| float                      | 56.8 ms                                                     | 55.5 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| raytrace                   | 192 ms                                                      | 193 ms: 1.01x slower                                                       |
| pathlib                    | 80.5 ms                                                     | 81.2 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.37 us: 1.02x slower                                                      |
| chaos                      | 43.3 ms                                                     | 44.3 ms: 1.02x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.88 us: 1.02x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 95.4 ms: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.4 ms: 1.04x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 65.1 ms: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 299 ms: 1.06x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 92.3 ms: 1.06x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 59.0 ms: 1.06x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 198 ms: 1.06x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 94.9 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.6 ms: 1.06x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                      |
| 2to3                       | 218 ms                                                      | 233 ms: 1.07x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 69.7 ms: 1.07x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 64.7 ns: 1.07x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.07x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 52.1 ms: 1.08x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                      |
| json                       | 3.05 ms                                                     | 3.32 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 73.0 ms: 1.09x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 878 us: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.81 ms: 1.10x slower                                                      |
| go                         | 91.6 ms                                                     | 101 ms: 1.10x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 535 ms: 1.10x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 64.7 ms: 1.10x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 215 us: 1.10x slower                                                       |
| scimark_fft                | 184 ms                                                      | 203 ms: 1.10x slower                                                       |
| pyflate                    | 295 ms                                                      | 325 ms: 1.10x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.7 ms: 1.11x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.53 sec: 1.11x slower                                                     |
| json_dumps                 | 5.70 ms                                                     | 6.34 ms: 1.11x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.59 ms: 1.12x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 575 ms: 1.12x slower                                                       |
| python_startup             | 19.5 ms                                                     | 21.9 ms: 1.12x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.18 sec: 1.13x slower                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.8 ms: 1.14x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.3 ms: 1.16x slower                                                      |
| nbody                      | 71.9 ms                                                     | 84.9 ms: 1.18x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 93.1 ms: 1.18x slower                                                      |
| richards_super             | 32.1 ms                                                     | 37.9 ms: 1.18x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                     |
| richards                   | 28.4 ms                                                     | 33.7 ms: 1.19x slower                                                      |
| fannkuch                   | 247 ms                                                      | 297 ms: 1.20x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.99 ms: 1.21x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 920 us: 1.22x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 118 us: 1.24x slower                                                       |
| pycparser                  | 699 ms                                                      | 892 ms: 1.28x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (2): coroutines, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240810-3.14.0a0-363374c/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown