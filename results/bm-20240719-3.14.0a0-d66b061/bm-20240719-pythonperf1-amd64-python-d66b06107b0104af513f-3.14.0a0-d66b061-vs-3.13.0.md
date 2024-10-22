# Results vs. 3.13.0

- fork: python
- ref: d66b06107b0104af513f
- machine: windows-amd64
- commit hash: d66b061
- commit date: 2024-07-19
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.4 ms: 1.05x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 91.2 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 534 ms: 1.22x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 244 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 189 ms: 1.09x faster                                                       |
| async_tree_none            | 223 ms                                                      | 210 ms: 1.06x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 256 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 386 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 532 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                      |
| async_tree_io              | 521 ms                                                      | 552 ms: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 55.4 ms: 1.15x slower                                                      |
| nbody          | 64.5 ms                                                     | 78.2 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 85.8 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.2 us: 1.01x faster                                                      |
| json_dumps           | 5.76 ms                                                     | 5.90 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.3 ms: 1.03x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.2 ms: 1.07x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.5 ms: 1.08x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 199 us: 1.08x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 139 us: 1.09x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.50 sec: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.4 ms: 1.04x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 17.5 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 33.8 ms: 1.03x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 15.8 ms: 1.06x slower                                                      |
| django_template | 21.8 ms                                                     | 23.2 ms: 1.07x slower                                                      |
| mako            | 6.24 ms                                                     | 7.08 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 525 us: 16.54x faster                                                      |
| deepcopy                   | 223 us                                                      | 174 us: 1.28x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 534 ms: 1.22x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 244 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 19.6 us: 1.11x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 189 ms: 1.09x faster                                                       |
| async_tree_none            | 223 ms                                                      | 210 ms: 1.06x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 256 ms: 1.06x faster                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 67.1 ms: 1.04x faster                                                      |
| python_startup             | 22.2 ms                                                     | 21.4 ms: 1.04x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 800 us: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| tornado_http               | 92.8 ms                                                     | 91.2 ms: 1.02x faster                                                      |
| json                       | 2.98 ms                                                     | 2.94 ms: 1.02x faster                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 17.5 ms: 1.01x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 80.3 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.2 us: 1.01x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.82 ms: 1.01x faster                                                      |
| coverage                   | 46.7 ms                                                     | 47.3 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 73.8 ms: 1.02x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 5.90 ms: 1.02x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 88.7 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 386 ms: 1.03x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 33.8 ms: 1.03x slower                                                      |
| 2to3                       | 217 ms                                                      | 224 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.3 ms: 1.03x slower                                                      |
| sympy_expand               | 285 ms                                                      | 294 ms: 1.03x slower                                                       |
| sympy_str                  | 166 ms                                                      | 172 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 532 ms: 1.04x slower                                                       |
| regex_dna                  | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                      |
| logging_simple             | 5.72 us                                                     | 5.98 us: 1.04x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 34.6 ms: 1.05x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 40.4 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 105 us: 1.05x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.46 us: 1.05x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.46 sec: 1.05x slower                                                     |
| sqlglot_normalize          | 171 ms                                                      | 181 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                      |
| async_tree_io              | 521 ms                                                      | 552 ms: 1.06x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 523 ms: 1.06x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                                     |
| generators                 | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 15.8 ms: 1.06x slower                                                      |
| django_template            | 21.8 ms                                                     | 23.2 ms: 1.07x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 85.8 ms: 1.07x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 57.2 ms: 1.07x slower                                                      |
| go                         | 84.6 ms                                                     | 91.0 ms: 1.08x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.07 sec: 1.08x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 39.5 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 58.6 ms: 1.08x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 199 us: 1.08x slower                                                       |
| comprehensions             | 10.2 us                                                     | 11.1 us: 1.08x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 903 us: 1.09x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 60.7 ms: 1.09x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 139 us: 1.09x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.5 ms: 1.09x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.04 ms: 1.09x slower                                                      |
| pyflate                    | 275 ms                                                      | 302 ms: 1.10x slower                                                       |
| richards                   | 26.0 ms                                                     | 28.6 ms: 1.10x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.50 sec: 1.10x slower                                                     |
| raytrace                   | 156 ms                                                      | 172 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.06 ms: 1.11x slower                                                      |
| richards_super             | 29.3 ms                                                     | 32.7 ms: 1.12x slower                                                      |
| pycparser                  | 758 ms                                                      | 848 ms: 1.12x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.14 ms: 1.12x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 854 us: 1.12x slower                                                       |
| mako                       | 6.24 ms                                                     | 7.08 ms: 1.14x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 48.6 ms: 1.14x slower                                                      |
| scimark_fft                | 174 ms                                                      | 199 ms: 1.14x slower                                                       |
| fannkuch                   | 245 ms                                                      | 280 ms: 1.15x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 58.4 ns: 1.15x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 46.4 ms: 1.15x slower                                                      |
| float                      | 48.1 ms                                                     | 55.4 ms: 1.15x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 68.9 ms: 1.16x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.73 ms: 1.17x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 84.4 ms: 1.17x slower                                                      |
| nbody                      | 64.5 ms                                                     | 78.2 ms: 1.21x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (6): asyncio_tcp_ssl, async_tree_cpu_io_mixed, pylint, xml_etree_parse, regex_v8, gc_traversal
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown