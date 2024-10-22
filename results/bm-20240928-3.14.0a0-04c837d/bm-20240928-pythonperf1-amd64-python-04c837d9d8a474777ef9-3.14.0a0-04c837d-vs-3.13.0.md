# Results vs. 3.13.0

- fork: python
- ref: 04c837d9d8a474777ef9
- machine: windows-amd64
- commit hash: 04c837d
- commit date: 2024-09-28
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 227 ms: 1.05x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.8 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 526 ms: 1.24x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| async_tree_none            | 223 ms                                                      | 211 ms: 1.06x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 262 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 392 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 563 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 56.2 ms: 1.17x slower                                                      |
| nbody          | 64.5 ms                                                     | 89.4 ms: 1.39x slower                                                      |
| Geometric mean | (ref)                                                       | 1.18x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 14.9 ms: 1.02x slower                                                      |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 92.9 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.19 us: 1.02x faster                                                      |
| json_loads           | 14.3 us                                                     | 14.1 us: 1.01x faster                                                      |
| pickle_dict          | 18.0 us                                                     | 18.5 us: 1.02x slower                                                      |
| pickle_list          | 2.89 us                                                     | 3.01 us: 1.04x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.86 us: 1.05x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.1 ms: 1.06x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.24 us: 1.07x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 58.4 ms: 1.09x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.43 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.6 ms: 1.14x slower                                                      |
| tomli_loads          | 1.36 sec                                                    | 1.63 sec: 1.20x slower                                                     |
| pickle_pure_python   | 183 us                                                      | 221 us: 1.21x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 156 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.8 ms: 1.09x slower                                                      |
| mako            | 6.24 ms                                                     | 6.88 ms: 1.10x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| django_template | 21.8 ms                                                     | 25.6 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 535 us: 16.22x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 526 ms: 1.24x faster                                                       |
| deepcopy                   | 223 us                                                      | 190 us: 1.18x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| async_tree_none            | 223 ms                                                      | 211 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.03x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 262 ms: 1.03x faster                                                       |
| pickle                     | 7.34 us                                                     | 7.19 us: 1.02x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.1 us: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.54 ms: 1.01x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 80.2 ms: 1.01x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 21.6 us: 1.01x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 69.1 ms: 1.01x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.91 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.01x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 14.9 ms: 1.02x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.63 us: 1.02x slower                                                      |
| coverage                   | 46.7 ms                                                     | 47.7 ms: 1.02x slower                                                      |
| pickle_dict                | 18.0 us                                                     | 18.5 us: 1.02x slower                                                      |
| regex_dna                  | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| pickle_list                | 2.89 us                                                     | 3.01 us: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 392 ms: 1.05x slower                                                       |
| 2to3                       | 217 ms                                                      | 227 ms: 1.05x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 90.5 ms: 1.05x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.86 us: 1.05x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 40.8 ms: 1.06x slower                                                      |
| go                         | 84.6 ms                                                     | 89.7 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.1 ms: 1.06x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.24 us: 1.07x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 889 us: 1.07x slower                                                       |
| sympy_str                  | 166 ms                                                      | 179 ms: 1.07x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                     |
| sympy_expand               | 285 ms                                                      | 310 ms: 1.09x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 43.9 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 109 us: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 35.8 ms: 1.09x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 58.4 ms: 1.09x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 563 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                       |
| mako                       | 6.24 ms                                                     | 6.88 ms: 1.10x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 79.9 ms: 1.11x slower                                                      |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 36.8 ms: 1.11x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.43 ms: 1.12x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.90 us: 1.12x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.55 sec: 1.12x slower                                                     |
| logging_simple             | 5.72 us                                                     | 6.47 us: 1.13x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.6 ms: 1.14x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 195 ms: 1.14x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 564 ms: 1.15x slower                                                       |
| unpack_sequence            | 40.0 ns                                                     | 45.8 ns: 1.15x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 49.4 ms: 1.15x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.15 sec: 1.16x slower                                                     |
| regex_compile              | 80.1 ms                                                     | 92.9 ms: 1.16x slower                                                      |
| float                      | 48.1 ms                                                     | 56.2 ms: 1.17x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 69.2 ms: 1.17x slower                                                      |
| django_template            | 21.8 ms                                                     | 25.6 ms: 1.18x slower                                                      |
| scimark_fft                | 174 ms                                                      | 205 ms: 1.18x slower                                                       |
| chaos                      | 37.9 ms                                                     | 44.7 ms: 1.18x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 65.8 ms: 1.19x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.13 ms: 1.19x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 906 us: 1.19x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.80 ms: 1.20x slower                                                      |
| pyflate                    | 275 ms                                                      | 330 ms: 1.20x slower                                                       |
| comprehensions             | 10.2 us                                                     | 12.3 us: 1.20x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.63 sec: 1.20x slower                                                     |
| pickle_pure_python         | 183 us                                                      | 221 us: 1.21x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 156 us: 1.23x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.32 ms: 1.25x slower                                                      |
| raytrace                   | 156 ms                                                      | 196 ms: 1.25x slower                                                       |
| fannkuch                   | 245 ms                                                      | 308 ms: 1.26x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 68.1 ms: 1.26x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.70 ms: 1.27x slower                                                      |
| richards_super             | 29.3 ms                                                     | 37.4 ms: 1.27x slower                                                      |
| richards                   | 26.0 ms                                                     | 33.3 ms: 1.28x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 51.6 ms: 1.28x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 65.4 ns: 1.28x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 95.5 ms: 1.33x slower                                                      |
| nbody                      | 64.5 ms                                                     | 89.4 ms: 1.39x slower                                                      |
| json                       | 2.98 ms                                                     | 4.24 ms: 1.42x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, pycparser, async_tree_none_tg, bench_thread_pool, tornado_http, async_tree_cpu_io_mixed, python_startup, xml_etree_parse, python_startup_no_site, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown