# Results vs. 3.13.0

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: windows-amd64
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 229 ms: 1.05x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.72 sec: 1.09x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.9 ms: 1.11x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 94.9 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 568 ms: 1.15x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                       |
| async_tree_none            | 223 ms                                                      | 214 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 396 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 391 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 579 ms: 1.13x slower                                                       |
| async_tree_io              | 521 ms                                                      | 591 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (3): async_tree_memoization, asyncio_tcp_ssl, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 48.1 ms                                                     | 53.8 ms: 1.12x slower                                                      |
| nbody          | 64.5 ms                                                     | 79.3 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 15.3 ms: 1.05x slower                                                      |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.3 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.25 us: 1.01x faster                                                      |
| json_loads           | 14.3 us                                                     | 14.7 us: 1.03x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.80 us: 1.03x slower                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 96.5 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.3 ms: 1.06x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 19.2 us: 1.07x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.4 ms: 1.08x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.40 us: 1.09x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 40.2 ms: 1.10x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 148 us: 1.17x slower                                                       |
| json_dumps           | 5.76 ms                                                     | 6.75 ms: 1.17x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 220 us: 1.20x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.64 sec: 1.20x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.2 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.78 ms: 1.09x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 37.0 ms: 1.13x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| django_template | 21.8 ms                                                     | 25.7 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 516 us: 16.83x faster                                                      |
| deepcopy                   | 223 us                                                      | 193 us: 1.16x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 568 ms: 1.15x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                       |
| unpack_sequence            | 40.0 ns                                                     | 36.0 ns: 1.11x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 19.7 us: 1.11x faster                                                      |
| async_tree_none            | 223 ms                                                      | 214 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 812 us: 1.02x faster                                                       |
| gc_traversal               | 1.55 ms                                                     | 1.53 ms: 1.01x faster                                                      |
| pickle                     | 7.34 us                                                     | 7.25 us: 1.01x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 2.00 us: 1.01x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 80.4 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 396 ms: 1.02x slower                                                       |
| go                         | 84.6 ms                                                     | 86.4 ms: 1.02x slower                                                      |
| tornado_http               | 92.8 ms                                                     | 94.9 ms: 1.02x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.2 ms: 1.02x slower                                                      |
| json_loads                 | 14.3 us                                                     | 14.7 us: 1.03x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.80 us: 1.03x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 96.5 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 391 ms: 1.04x slower                                                       |
| sqlite_synth               | 1.60 us                                                     | 1.67 us: 1.04x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 15.3 ms: 1.05x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 90.9 ms: 1.05x slower                                                      |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| 2to3                       | 217 ms                                                      | 229 ms: 1.05x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 76.6 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.3 ms: 1.06x slower                                                      |
| pickle_dict                | 18.0 us                                                     | 19.2 us: 1.07x slower                                                      |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 57.4 ms: 1.08x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 58.4 ms: 1.08x slower                                                      |
| sympy_expand               | 285 ms                                                      | 309 ms: 1.09x slower                                                       |
| mako                       | 6.24 ms                                                     | 6.78 ms: 1.09x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.40 us: 1.09x slower                                                      |
| pylint                     | 211 ms                                                      | 230 ms: 1.09x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.72 sec: 1.09x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 40.2 ms: 1.10x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 44.5 ms: 1.10x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.5 ms: 1.11x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 42.9 ms: 1.11x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 112 us: 1.11x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 547 ms: 1.11x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.85 us: 1.11x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 923 us: 1.11x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.38 us: 1.11x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 36.9 ms: 1.12x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| float                      | 48.1 ms                                                     | 53.8 ms: 1.12x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.55 sec: 1.12x slower                                                     |
| crypto_pyaes               | 42.8 ms                                                     | 48.1 ms: 1.12x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 37.0 ms: 1.13x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| async_tree_io_tg           | 512 ms                                                      | 579 ms: 1.13x slower                                                       |
| async_tree_io              | 521 ms                                                      | 591 ms: 1.13x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 91.3 ms: 1.14x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 196 ms: 1.14x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.68 ms: 1.15x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| fannkuch                   | 245 ms                                                      | 282 ms: 1.15x slower                                                       |
| comprehensions             | 10.2 us                                                     | 11.8 us: 1.15x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 68.3 ms: 1.15x slower                                                      |
| chaos                      | 37.9 ms                                                     | 43.7 ms: 1.15x slower                                                      |
| pyflate                    | 275 ms                                                      | 318 ms: 1.16x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 46.7 ms: 1.16x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 64.4 ms: 1.16x slower                                                      |
| scimark_fft                | 174 ms                                                      | 203 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 148 us: 1.17x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.75 ms: 1.17x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.33 ms: 1.17x slower                                                      |
| django_template            | 21.8 ms                                                     | 25.7 ms: 1.18x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 60.7 ns: 1.19x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 908 us: 1.19x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.14 ms: 1.19x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 220 us: 1.20x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.64 sec: 1.20x slower                                                     |
| deltablue                  | 1.86 ms                                                     | 2.26 ms: 1.21x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 88.2 ms: 1.22x slower                                                      |
| nbody                      | 64.5 ms                                                     | 79.3 ms: 1.23x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.1 ms: 1.23x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.2 ms: 1.24x slower                                                      |
| raytrace                   | 156 ms                                                      | 207 ms: 1.33x slower                                                       |
| json                       | 2.98 ms                                                     | 4.18 ms: 1.40x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (10): pycparser, bench_mp_pool, telco, coverage, async_tree_memoization, pidigits, asyncio_tcp_ssl, python_startup, async_tree_none_tg, pickle_list
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown