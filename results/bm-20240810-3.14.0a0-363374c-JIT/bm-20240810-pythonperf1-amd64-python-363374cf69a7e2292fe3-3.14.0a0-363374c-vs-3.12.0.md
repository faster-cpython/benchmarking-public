# Results vs. 3.12.0

- fork: python
- ref: 363374cf69a7e2292fe3
- machine: windows-amd64
- commit hash: 363374c
- commit date: 2024-08-10
- overall geometric mean: 1.05x faster
- HPT reliability: 91.83%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 240 ms: 1.10x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.85 sec: 1.12x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 96.1 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 196 ms: 1.46x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 547 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 215 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                       |
| async_tree_io              | 731 ms                                                      | 576 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.0 ms: 1.44x faster                                                      |
| float          | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 90.0 ms: 1.03x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|---------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads         | 1.37 sec                                                    | 1.27 sec: 1.07x faster                                                     |
| pickle_pure_python  | 195 us                                                      | 182 us: 1.07x faster                                                       |
| xml_etree_generate  | 55.8 ms                                                     | 52.9 ms: 1.06x faster                                                      |
| xml_etree_iterparse | 65.2 ms                                                     | 62.2 ms: 1.05x faster                                                      |
| xml_etree_process   | 37.7 ms                                                     | 38.0 ms: 1.01x slower                                                      |
| xml_etree_parse     | 93.0 ms                                                     | 94.9 ms: 1.02x slower                                                      |
| json_loads          | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| json_dumps          | 5.70 ms                                                     | 5.94 ms: 1.04x slower                                                      |
| Geometric mean      | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.08 ms: 1.40x faster                                                      |
| django_template | 22.9 ms                                                     | 25.1 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 196 ms: 1.46x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 16.3 us: 1.45x faster                                                      |
| nbody                      | 71.9 ms                                                     | 50.0 ms: 1.44x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 46.7 ms: 1.43x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 547 ms: 1.41x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.08 ms: 1.40x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                      |
| async_tree_none            | 291 ms                                                      | 215 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                       |
| deepcopy                   | 238 us                                                      | 184 us: 1.30x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 61.5 ms: 1.28x faster                                                      |
| async_tree_io              | 731 ms                                                      | 576 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.24x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.0 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.13 ms: 1.20x faster                                                      |
| pyflate                    | 295 ms                                                      | 248 ms: 1.19x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.7 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                      |
| fannkuch                   | 247 ms                                                      | 217 ms: 1.14x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.3 ms: 1.10x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 475 ms: 1.08x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.27 sec: 1.07x faster                                                     |
| pprint_pformat             | 1.05 sec                                                    | 975 ms: 1.07x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 182 us: 1.07x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.5 ns: 1.07x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 55.3 ms: 1.06x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 52.9 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.2 ms: 1.05x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.01 us: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.7 ms: 1.04x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.48 us: 1.04x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.9 ms: 1.03x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.6 ms: 1.02x faster                                                      |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.0 ms: 1.01x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| pathlib                    | 80.5 ms                                                     | 81.6 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.9 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 90.0 ms: 1.03x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 828 us: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.04x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.94 ms: 1.04x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.59 ms: 1.04x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                     |
| sympy_sum                  | 91.5 ms                                                     | 96.9 ms: 1.06x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 73.4 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 37.0 ms: 1.07x slower                                                      |
| sympy_str                  | 175 ms                                                      | 188 ms: 1.07x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 96.1 ms: 1.07x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                      |
| async_generators           | 239 ms                                                      | 260 ms: 1.09x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                      |
| richards                   | 28.4 ms                                                     | 31.1 ms: 1.09x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.10x slower                                                      |
| go                         | 91.6 ms                                                     | 100 ms: 1.10x slower                                                       |
| richards_super             | 32.1 ms                                                     | 35.2 ms: 1.10x slower                                                      |
| 2to3                       | 218 ms                                                      | 240 ms: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.59 ms: 1.11x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.85 sec: 1.12x slower                                                     |
| asyncio_tcp                | 487 ms                                                      | 550 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.7 ms: 1.14x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.8 ms: 1.15x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.75 ms: 1.16x slower                                                      |
| sympy_expand               | 284 ms                                                      | 330 ms: 1.16x slower                                                       |
| pycparser                  | 699 ms                                                      | 851 ms: 1.22x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 117 us: 1.23x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 927 us: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (3): bench_thread_pool, unpickle_pure_python, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240810-3.14.0a0-363374c-JIT/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 91.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown