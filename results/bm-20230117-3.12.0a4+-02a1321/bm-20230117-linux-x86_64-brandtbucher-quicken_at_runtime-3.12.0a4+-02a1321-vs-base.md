
# Results vs. base

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 02a1321
- commit date: 2023-01-17
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 256 ms: 1.02x slower                                                       |
| chameleon      | 6.42 ms                                                                | 6.32 ms: 1.02x faster                                                      |
| tornado_http   | 93.7 ms                                                                | 94.4 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                 | 193 ms: 1.03x faster                                                       |
| nbody          | 92.9 ms                                                                | 94.0 ms: 1.01x slower                                                      |
| float          | 72.1 ms                                                                | 76.0 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 22.6 ms                                                                | 21.5 ms: 1.05x faster                                                      |
| regex_dna      | 210 ms                                                                 | 209 ms: 1.01x faster                                                       |
| regex_effbot   | 3.48 ms                                                                | 3.65 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 78.6 ms                                                                | 76.9 ms: 1.02x faster                                                      |
| xml_etree_process    | 54.2 ms                                                                | 53.2 ms: 1.02x faster                                                      |
| unpickle_list        | 5.01 us                                                                | 4.93 us: 1.02x faster                                                      |
| json_dumps           | 9.46 ms                                                                | 9.34 ms: 1.01x faster                                                      |
| json_loads           | 24.1 us                                                                | 23.9 us: 1.01x faster                                                      |
| unpickle             | 13.1 us                                                                | 13.0 us: 1.01x faster                                                      |
| pickle               | 9.90 us                                                                | 10.1 us: 1.01x slower                                                      |
| pickle_list          | 4.00 us                                                                | 4.08 us: 1.02x slower                                                      |
| pickle_dict          | 30.1 us                                                                | 30.8 us: 1.02x slower                                                      |
| xml_etree_parse      | 148 ms                                                                 | 151 ms: 1.02x slower                                                       |
| pickle_pure_python   | 284 us                                                                 | 293 us: 1.03x slower                                                       |
| unpickle_pure_python | 196 us                                                                 | 209 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.46 ms                                                                | 6.27 ms: 1.03x faster                                                      |
| python_startup         | 8.93 ms                                                                | 8.74 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 20.6 ms                                                                | 20.2 ms: 1.02x faster                                                      |
| genshi_xml     | 47.2 ms                                                                | 46.2 ms: 1.02x faster                                                      |
| mako           | 9.61 ms                                                                | 9.71 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal            | 4.16 ms                                                                | 3.59 ms: 1.16x faster                                                      |
| regex_v8                | 22.6 ms                                                                | 21.5 ms: 1.05x faster                                                      |
| python_startup_no_site  | 6.46 ms                                                                | 6.27 ms: 1.03x faster                                                      |
| pidigits                | 198 ms                                                                 | 193 ms: 1.03x faster                                                       |
| pycparser               | 1.14 sec                                                               | 1.11 sec: 1.02x faster                                                     |
| crypto_pyaes            | 73.8 ms                                                                | 72.0 ms: 1.02x faster                                                      |
| genshi_text             | 20.6 ms                                                                | 20.2 ms: 1.02x faster                                                      |
| python_startup          | 8.93 ms                                                                | 8.74 ms: 1.02x faster                                                      |
| xml_etree_generate      | 78.6 ms                                                                | 76.9 ms: 1.02x faster                                                      |
| genshi_xml              | 47.2 ms                                                                | 46.2 ms: 1.02x faster                                                      |
| xml_etree_process       | 54.2 ms                                                                | 53.2 ms: 1.02x faster                                                      |
| unpickle_list           | 5.01 us                                                                | 4.93 us: 1.02x faster                                                      |
| json                    | 4.63 ms                                                                | 4.56 ms: 1.02x faster                                                      |
| chameleon               | 6.42 ms                                                                | 6.32 ms: 1.02x faster                                                      |
| meteor_contest          | 108 ms                                                                 | 106 ms: 1.02x faster                                                       |
| json_dumps              | 9.46 ms                                                                | 9.34 ms: 1.01x faster                                                      |
| pathlib                 | 17.9 ms                                                                | 17.7 ms: 1.01x faster                                                      |
| async_generators        | 354 ms                                                                 | 350 ms: 1.01x faster                                                       |
| thrift                  | 746 us                                                                 | 738 us: 1.01x faster                                                       |
| json_loads              | 24.1 us                                                                | 23.9 us: 1.01x faster                                                      |
| regex_dna               | 210 ms                                                                 | 209 ms: 1.01x faster                                                       |
| asyncio_tcp             | 497 ms                                                                 | 494 ms: 1.01x faster                                                       |
| deepcopy_memo           | 34.3 us                                                                | 34.1 us: 1.01x faster                                                      |
| logging_silent          | 90.1 ns                                                                | 89.6 ns: 1.01x faster                                                      |
| deepcopy                | 328 us                                                                 | 326 us: 1.01x faster                                                       |
| unpickle                | 13.1 us                                                                | 13.0 us: 1.01x faster                                                      |
| generators              | 75.0 ms                                                                | 75.2 ms: 1.00x slower                                                      |
| mdp                     | 2.61 sec                                                               | 2.61 sec: 1.00x slower                                                     |
| dulwich_log             | 62.2 ms                                                                | 62.4 ms: 1.00x slower                                                      |
| coverage                | 96.2 ms                                                                | 96.7 ms: 1.01x slower                                                      |
| sympy_str               | 269 ms                                                                 | 271 ms: 1.01x slower                                                       |
| bench_thread_pool       | 776 us                                                                 | 782 us: 1.01x slower                                                       |
| tornado_http            | 93.7 ms                                                                | 94.4 ms: 1.01x slower                                                      |
| sqlglot_parse           | 1.40 ms                                                                | 1.41 ms: 1.01x slower                                                      |
| sympy_expand            | 451 ms                                                                 | 455 ms: 1.01x slower                                                       |
| sqlglot_transpile       | 1.69 ms                                                                | 1.71 ms: 1.01x slower                                                      |
| sqlglot_optimize        | 50.6 ms                                                                | 51.1 ms: 1.01x slower                                                      |
| mako                    | 9.61 ms                                                                | 9.71 ms: 1.01x slower                                                      |
| chaos                   | 64.0 ms                                                                | 64.7 ms: 1.01x slower                                                      |
| nbody                   | 92.9 ms                                                                | 94.0 ms: 1.01x slower                                                      |
| sympy_integrate         | 19.7 ms                                                                | 20.0 ms: 1.01x slower                                                      |
| logging_simple          | 5.73 us                                                                | 5.81 us: 1.01x slower                                                      |
| sqlglot_normalize       | 104 ms                                                                 | 105 ms: 1.01x slower                                                       |
| unpack_sequence         | 42.8 ns                                                                | 43.5 ns: 1.01x slower                                                      |
| pickle                  | 9.90 us                                                                | 10.1 us: 1.01x slower                                                      |
| telco                   | 6.24 ms                                                                | 6.34 ms: 1.02x slower                                                      |
| deepcopy_reduce         | 2.90 us                                                                | 2.95 us: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 751 ms                                                                 | 763 ms: 1.02x slower                                                       |
| go                      | 136 ms                                                                 | 139 ms: 1.02x slower                                                       |
| logging_format          | 6.33 us                                                                | 6.45 us: 1.02x slower                                                      |
| 2to3                    | 251 ms                                                                 | 256 ms: 1.02x slower                                                       |
| create_gc_cycles        | 1.45 ms                                                                | 1.48 ms: 1.02x slower                                                      |
| pickle_list             | 4.00 us                                                                | 4.08 us: 1.02x slower                                                      |
| coroutines              | 25.0 ms                                                                | 25.6 ms: 1.02x slower                                                      |
| pickle_dict             | 30.1 us                                                                | 30.8 us: 1.02x slower                                                      |
| xml_etree_parse         | 148 ms                                                                 | 151 ms: 1.02x slower                                                       |
| dask                    | 496 ms                                                                 | 512 ms: 1.03x slower                                                       |
| spectral_norm           | 94.4 ms                                                                | 97.5 ms: 1.03x slower                                                      |
| pickle_pure_python      | 284 us                                                                 | 293 us: 1.03x slower                                                       |
| nqueens                 | 75.4 ms                                                                | 78.0 ms: 1.03x slower                                                      |
| async_tree_memoization  | 616 ms                                                                 | 637 ms: 1.03x slower                                                       |
| scimark_monte_carlo     | 66.8 ms                                                                | 69.8 ms: 1.04x slower                                                      |
| scimark_fft             | 297 ms                                                                 | 310 ms: 1.04x slower                                                       |
| regex_effbot            | 3.48 ms                                                                | 3.65 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult | 4.06 ms                                                                | 4.26 ms: 1.05x slower                                                      |
| float                   | 72.1 ms                                                                | 76.0 ms: 1.05x slower                                                      |
| raytrace                | 283 ms                                                                 | 299 ms: 1.06x slower                                                       |
| fannkuch                | 363 ms                                                                 | 385 ms: 1.06x slower                                                       |
| unpickle_pure_python    | 196 us                                                                 | 209 us: 1.07x slower                                                       |
| pyflate                 | 393 ms                                                                 | 420 ms: 1.07x slower                                                       |
| deltablue               | 3.24 ms                                                                | 3.50 ms: 1.08x slower                                                      |
| richards                | 42.0 ms                                                                | 46.6 ms: 1.11x slower                                                      |
| scimark_sor             | 106 ms                                                                 | 119 ms: 1.13x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (18): xml_etree_iterparse, async_tree_none, sympy_sum, async_tree_io, pprint_safe_repr, docutils, bench_mp_pool, pprint_pformat, scimark_lu, aiohttp, django_template, gunicorn, hexiom, sqlite_synth, regex_compile, djangocms, mypy, html5lib
