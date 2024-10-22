# Results vs. 3.13.0

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: windows-amd64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.00x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                                     |
| html5lib       | 38.6 ms                                                     | 39.4 ms: 1.02x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 91.1 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 528 ms: 1.24x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 241 ms: 1.19x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 186 ms: 1.11x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 250 ms: 1.08x faster                                                       |
| async_tree_none            | 223 ms                                                      | 207 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 381 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 383 ms: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                                      |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 54.3 ms: 1.13x slower                                                      |
| nbody          | 64.5 ms                                                     | 75.2 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 85.0 ms: 1.06x slower                                                      |
| regex_v8       | 14.7 ms                                                     | 15.8 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 5.76 ms                                                     | 5.80 ms: 1.01x slower                                                      |
| json_loads           | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.8 ms: 1.04x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 56.0 ms: 1.05x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.5 ms: 1.05x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 193 us: 1.05x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 136 us: 1.07x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.49 sec: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 33.8 ms: 1.03x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 15.5 ms: 1.04x slower                                                      |
| django_template | 21.8 ms                                                     | 22.9 ms: 1.05x slower                                                      |
| mako            | 6.24 ms                                                     | 6.88 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 514 us: 16.88x faster                                                      |
| deepcopy                   | 223 us                                                      | 177 us: 1.26x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 528 ms: 1.24x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 241 ms: 1.19x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 18.9 us: 1.16x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 186 ms: 1.11x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 250 ms: 1.08x faster                                                       |
| async_tree_none            | 223 ms                                                      | 207 ms: 1.08x faster                                                       |
| bench_thread_pool          | 828 us                                                      | 793 us: 1.04x faster                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 67.4 ms: 1.03x faster                                                      |
| python_startup             | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                      |
| tornado_http               | 92.8 ms                                                     | 91.1 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 381 ms: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 80.3 ms: 1.01x faster                                                      |
| json                       | 2.98 ms                                                     | 2.96 ms: 1.01x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.81 ms: 1.01x faster                                                      |
| json_dumps                 | 5.76 ms                                                     | 5.80 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| 2to3                       | 217 ms                                                      | 220 ms: 1.01x slower                                                       |
| json_loads                 | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 88.0 ms: 1.02x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 33.6 ms: 1.02x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 39.4 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 383 ms: 1.02x slower                                                       |
| sympy_expand               | 285 ms                                                      | 292 ms: 1.02x slower                                                       |
| sympy_str                  | 166 ms                                                      | 170 ms: 1.03x slower                                                       |
| logging_simple             | 5.72 us                                                     | 5.88 us: 1.03x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.33 us: 1.03x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 33.8 ms: 1.03x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 74.9 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 104 us: 1.04x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.04x slower                                                      |
| regex_dna                  | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.8 ms: 1.04x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 178 ms: 1.04x slower                                                       |
| go                         | 84.6 ms                                                     | 88.1 ms: 1.04x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 15.5 ms: 1.04x slower                                                      |
| django_template            | 21.8 ms                                                     | 22.9 ms: 1.05x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 56.0 ms: 1.05x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.5 ms: 1.05x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 193 us: 1.05x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 85.0 ms: 1.06x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                                     |
| mdp                        | 1.38 sec                                                    | 1.47 sec: 1.06x slower                                                     |
| generators                 | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.06 sec: 1.07x slower                                                     |
| deltablue                  | 1.86 ms                                                     | 1.99 ms: 1.07x slower                                                      |
| richards                   | 26.0 ms                                                     | 27.8 ms: 1.07x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 136 us: 1.07x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 528 ms: 1.07x slower                                                       |
| comprehensions             | 10.2 us                                                     | 11.0 us: 1.07x slower                                                      |
| richards_super             | 29.3 ms                                                     | 31.6 ms: 1.08x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 15.8 ms: 1.08x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 3.98 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| raytrace                   | 156 ms                                                      | 169 ms: 1.08x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 899 us: 1.08x slower                                                       |
| pyflate                    | 275 ms                                                      | 299 ms: 1.09x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.49 sec: 1.09x slower                                                     |
| chaos                      | 37.9 ms                                                     | 41.4 ms: 1.09x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 60.8 ms: 1.09x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.04 ms: 1.10x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 59.4 ms: 1.10x slower                                                      |
| mako                       | 6.24 ms                                                     | 6.88 ms: 1.10x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 843 us: 1.11x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 47.7 ms: 1.11x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 57.1 ns: 1.12x slower                                                      |
| pycparser                  | 758 ms                                                      | 852 ms: 1.12x slower                                                       |
| float                      | 48.1 ms                                                     | 54.3 ms: 1.13x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 67.8 ms: 1.14x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 83.0 ms: 1.15x slower                                                      |
| nbody                      | 64.5 ms                                                     | 75.2 ms: 1.17x slower                                                      |
| fannkuch                   | 245 ms                                                      | 290 ms: 1.18x slower                                                       |
| scimark_fft                | 174 ms                                                      | 207 ms: 1.19x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 48.6 ms: 1.21x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.91 ms: 1.24x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (8): coverage, asyncio_tcp_ssl, python_startup_no_site, gc_traversal, xml_etree_parse, async_tree_io, async_tree_io_tg, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown