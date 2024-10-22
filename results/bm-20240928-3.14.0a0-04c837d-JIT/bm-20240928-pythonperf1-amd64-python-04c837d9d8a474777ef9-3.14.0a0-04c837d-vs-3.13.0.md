# Results vs. 3.13.0

- fork: python
- ref: 04c837d9d8a474777ef9
- machine: windows-amd64
- commit hash: 04c837d
- commit date: 2024-09-28
- overall geometric mean: 1.20x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 283 ms: 1.30x slower                                                       |
| docutils       | 1.57 sec                                                    | 2.18 sec: 1.39x slower                                                     |
| html5lib       | 38.6 ms                                                     | 47.9 ms: 1.24x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 106 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 569 ms: 1.15x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.54 sec: 1.06x faster                                                     |
| async_tree_none            | 223 ms                                                      | 237 ms: 1.06x slower                                                       |
| async_tree_memoization     | 271 ms                                                      | 297 ms: 1.09x slower                                                       |
| async_tree_none_tg         | 206 ms                                                      | 234 ms: 1.14x slower                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 454 ms: 1.17x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 449 ms: 1.20x slower                                                       |
| async_tree_io              | 521 ms                                                      | 647 ms: 1.24x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 639 ms: 1.25x slower                                                       |
| async_generators           | 223 ms                                                      | 336 ms: 1.51x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 19.6 ms: 1.56x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.15x slower                                                               |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 50.4 ms: 1.28x faster                                                      |
| pidigits       | 148 ms                                                      | 148 ms: 1.01x faster                                                       |
| float          | 48.1 ms                                                     | 55.8 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 114 ms                                                      | 117 ms: 1.03x slower                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.85 ms: 1.14x slower                                                      |
| regex_v8       | 14.7 ms                                                     | 16.9 ms: 1.16x slower                                                      |
| regex_compile  | 80.1 ms                                                     | 111 ms: 1.39x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 2.72 us                                                     | 2.92 us: 1.07x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 20.3 us: 1.12x slower                                                      |
| tomli_loads          | 1.36 sec                                                    | 1.53 sec: 1.12x slower                                                     |
| pickle               | 7.34 us                                                     | 8.42 us: 1.15x slower                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 109 ms: 1.17x slower                                                       |
| pickle_list          | 2.89 us                                                     | 3.41 us: 1.18x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 75.4 ms: 1.21x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 64.6 ms: 1.21x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 7.32 ms: 1.27x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 47.1 ms: 1.29x slower                                                      |
| unpickle             | 8.63 us                                                     | 11.9 us: 1.37x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 256 us: 1.39x slower                                                       |
| json_loads           | 14.3 us                                                     | 20.7 us: 1.44x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 204 us: 1.61x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 23.9 ms: 1.08x slower                                                      |
| python_startup_no_site | 17.8 ms                                                     | 19.7 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.05 ms: 1.03x faster                                                      |
| genshi_text     | 14.9 ms                                                     | 21.9 ms: 1.48x slower                                                      |
| django_template | 21.8 ms                                                     | 32.6 ms: 1.49x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 51.2 ms: 1.56x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.35x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 653 us: 13.29x faster                                                      |
| nbody                      | 64.5 ms                                                     | 50.4 ms: 1.28x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 18.6 us: 1.17x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 569 ms: 1.15x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.54 sec: 1.06x faster                                                     |
| deepcopy                   | 223 us                                                      | 214 us: 1.04x faster                                                       |
| mako                       | 6.24 ms                                                     | 6.05 ms: 1.03x faster                                                      |
| pidigits                   | 148 ms                                                      | 148 ms: 1.01x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 82.0 ms: 1.01x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 59.8 ms: 1.01x slower                                                      |
| regex_dna                  | 114 ms                                                      | 117 ms: 1.03x slower                                                       |
| scimark_fft                | 174 ms                                                      | 180 ms: 1.03x slower                                                       |
| async_tree_none            | 223 ms                                                      | 237 ms: 1.06x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 45.8 ms: 1.07x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.92 us: 1.07x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.19 ms: 1.07x slower                                                      |
| python_startup             | 22.2 ms                                                     | 23.9 ms: 1.08x slower                                                      |
| async_tree_memoization     | 271 ms                                                      | 297 ms: 1.09x slower                                                       |
| pyflate                    | 275 ms                                                      | 301 ms: 1.09x slower                                                       |
| pycparser                  | 758 ms                                                      | 837 ms: 1.10x slower                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 19.7 ms: 1.11x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 2.25 us: 1.11x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.78 us: 1.12x slower                                                      |
| pickle_dict                | 18.0 us                                                     | 20.3 us: 1.12x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.53 sec: 1.12x slower                                                     |
| bench_thread_pool          | 828 us                                                      | 933 us: 1.13x slower                                                       |
| async_tree_none_tg         | 206 ms                                                      | 234 ms: 1.14x slower                                                       |
| tornado_http               | 92.8 ms                                                     | 106 ms: 1.14x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.85 ms: 1.14x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.68 ms: 1.15x slower                                                      |
| pickle                     | 7.34 us                                                     | 8.42 us: 1.15x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 83.1 ms: 1.15x slower                                                      |
| fannkuch                   | 245 ms                                                      | 282 ms: 1.15x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 16.9 ms: 1.16x slower                                                      |
| float                      | 48.1 ms                                                     | 55.8 ms: 1.16x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 83.8 ms: 1.16x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 109 ms: 1.17x slower                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 454 ms: 1.17x slower                                                       |
| pickle_list                | 2.89 us                                                     | 3.41 us: 1.18x slower                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 82.8 ms: 1.19x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 449 ms: 1.20x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 75.4 ms: 1.21x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 64.6 ms: 1.21x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.68 sec: 1.22x slower                                                     |
| dulwich_log                | 40.4 ms                                                     | 49.2 ms: 1.22x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 1.01 ms: 1.22x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.30 ms: 1.23x slower                                                      |
| json                       | 2.98 ms                                                     | 3.68 ms: 1.23x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 47.9 ms: 1.24x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 612 ms: 1.24x slower                                                       |
| async_tree_io              | 521 ms                                                      | 647 ms: 1.24x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 639 ms: 1.25x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.24 sec: 1.25x slower                                                     |
| logging_format             | 6.15 us                                                     | 7.81 us: 1.27x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 51.1 ms: 1.27x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 7.32 ms: 1.27x slower                                                      |
| comprehensions             | 10.2 us                                                     | 13.2 us: 1.29x slower                                                      |
| logging_simple             | 5.72 us                                                     | 7.36 us: 1.29x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 47.1 ms: 1.29x slower                                                      |
| chaos                      | 37.9 ms                                                     | 48.9 ms: 1.29x slower                                                      |
| coverage                   | 46.7 ms                                                     | 60.8 ms: 1.30x slower                                                      |
| 2to3                       | 217 ms                                                      | 283 ms: 1.30x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 131 us: 1.31x slower                                                       |
| generators                 | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 118 ms: 1.36x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 75.6 ms: 1.36x slower                                                      |
| sympy_str                  | 166 ms                                                      | 227 ms: 1.37x slower                                                       |
| go                         | 84.6 ms                                                     | 116 ms: 1.37x slower                                                       |
| sympy_expand               | 285 ms                                                      | 390 ms: 1.37x slower                                                       |
| unpickle                   | 8.63 us                                                     | 11.9 us: 1.37x slower                                                      |
| docutils                   | 1.57 sec                                                    | 2.18 sec: 1.39x slower                                                     |
| regex_compile              | 80.1 ms                                                     | 111 ms: 1.39x slower                                                       |
| pickle_pure_python         | 183 us                                                      | 256 us: 1.39x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 239 ms: 1.40x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 1.06 ms: 1.40x slower                                                      |
| pylint                     | 211 ms                                                      | 299 ms: 1.42x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 17.5 ms: 1.42x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.37 ms: 1.44x slower                                                      |
| gc_traversal               | 1.55 ms                                                     | 2.24 ms: 1.44x slower                                                      |
| json_loads                 | 14.3 us                                                     | 20.7 us: 1.44x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 21.9 ms: 1.48x slower                                                      |
| django_template            | 21.8 ms                                                     | 32.6 ms: 1.49x slower                                                      |
| async_generators           | 223 ms                                                      | 336 ms: 1.51x slower                                                       |
| richards_super             | 29.3 ms                                                     | 44.2 ms: 1.51x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 50.0 ms: 1.51x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 61.0 ns: 1.52x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 84.0 ms: 1.56x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 19.6 ms: 1.56x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 51.2 ms: 1.56x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 204 us: 1.61x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 5.95 ms: 1.61x slower                                                      |
| raytrace                   | 156 ms                                                      | 253 ms: 1.62x slower                                                       |
| richards                   | 26.0 ms                                                     | 42.4 ms: 1.63x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 85.0 ns: 1.67x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.20x slower                                                               |

Benchmark hidden because not significant (1): async_tree_memoization_tg
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: unknown