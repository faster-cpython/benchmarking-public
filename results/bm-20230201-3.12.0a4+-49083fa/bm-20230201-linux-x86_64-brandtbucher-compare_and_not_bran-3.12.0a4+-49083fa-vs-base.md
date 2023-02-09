
# Results vs. base

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 49083fa
- commit date: 2023-02-01
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 253 ms: 1.00x faster                                                         |
| chameleon      | 6.59 ms                                                                | 6.47 ms: 1.02x faster                                                        |
| docutils       | 2.50 sec                                                               | 2.53 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 72.1 ms                                                                | 72.7 ms: 1.01x slower                                                        |
| nbody          | 92.9 ms                                                                | 94.4 ms: 1.02x slower                                                        |
| pidigits       | 189 ms                                                                 | 198 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 128 ms: 1.00x faster                                                         |
| regex_effbot   | 3.57 ms                                                                | 3.63 ms: 1.02x slower                                                        |
| regex_dna      | 209 ms                                                                 | 217 ms: 1.03x slower                                                         |
| regex_v8       | 21.1 ms                                                                | 22.5 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 78.5 ms                                                                | 78.0 ms: 1.01x faster                                                        |
| xml_etree_process    | 54.4 ms                                                                | 54.0 ms: 1.01x faster                                                        |
| pickle_pure_python   | 288 us                                                                 | 287 us: 1.00x faster                                                         |
| json_dumps           | 9.28 ms                                                                | 9.33 ms: 1.01x slower                                                        |
| pickle               | 10.0 us                                                                | 10.2 us: 1.02x slower                                                        |
| unpickle_pure_python | 198 us                                                                 | 202 us: 1.02x slower                                                         |
| xml_etree_iterparse  | 103 ms                                                                 | 107 ms: 1.04x slower                                                         |
| pickle_list          | 4.03 us                                                                | 4.31 us: 1.07x slower                                                        |
| pickle_dict          | 29.9 us                                                                | 32.2 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.48 ms                                                                | 6.43 ms: 1.01x faster                                                        |
| python_startup         | 8.95 ms                                                                | 8.88 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 20.9 ms                                                                | 20.6 ms: 1.01x faster                                                        |
| genshi_xml     | 46.6 ms                                                                | 46.3 ms: 1.01x faster                                                        |
| mako           | 9.69 ms                                                                | 9.75 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpack_sequence         | 46.8 ns                                                                | 43.0 ns: 1.09x faster                                                        |
| fannkuch                | 389 ms                                                                 | 367 ms: 1.06x faster                                                         |
| async_tree_memoization  | 667 ms                                                                 | 641 ms: 1.04x faster                                                         |
| deepcopy                | 332 us                                                                 | 321 us: 1.04x faster                                                         |
| raytrace                | 287 ms                                                                 | 280 ms: 1.03x faster                                                         |
| meteor_contest          | 108 ms                                                                 | 106 ms: 1.02x faster                                                         |
| chameleon               | 6.59 ms                                                                | 6.47 ms: 1.02x faster                                                        |
| hexiom                  | 6.03 ms                                                                | 5.92 ms: 1.02x faster                                                        |
| spectral_norm           | 95.2 ms                                                                | 93.4 ms: 1.02x faster                                                        |
| pathlib                 | 17.9 ms                                                                | 17.6 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 2.93 us                                                                | 2.88 us: 1.02x faster                                                        |
| nqueens                 | 77.8 ms                                                                | 76.6 ms: 1.02x faster                                                        |
| richards                | 42.2 ms                                                                | 41.5 ms: 1.01x faster                                                        |
| scimark_monte_carlo     | 67.0 ms                                                                | 66.1 ms: 1.01x faster                                                        |
| crypto_pyaes            | 74.6 ms                                                                | 73.7 ms: 1.01x faster                                                        |
| logging_simple          | 5.84 us                                                                | 5.77 us: 1.01x faster                                                        |
| genshi_text             | 20.9 ms                                                                | 20.6 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed | 761 ms                                                                 | 753 ms: 1.01x faster                                                         |
| coroutines              | 26.7 ms                                                                | 26.4 ms: 1.01x faster                                                        |
| sqlglot_optimize        | 51.5 ms                                                                | 50.9 ms: 1.01x faster                                                        |
| create_gc_cycles        | 1.48 ms                                                                | 1.46 ms: 1.01x faster                                                        |
| async_generators        | 357 ms                                                                 | 353 ms: 1.01x faster                                                         |
| sqlite_synth            | 2.61 us                                                                | 2.59 us: 1.01x faster                                                        |
| python_startup_no_site  | 6.48 ms                                                                | 6.43 ms: 1.01x faster                                                        |
| sympy_expand            | 457 ms                                                                 | 454 ms: 1.01x faster                                                         |
| python_startup          | 8.95 ms                                                                | 8.88 ms: 1.01x faster                                                        |
| genshi_xml              | 46.6 ms                                                                | 46.3 ms: 1.01x faster                                                        |
| logging_format          | 6.42 us                                                                | 6.38 us: 1.01x faster                                                        |
| xml_etree_generate      | 78.5 ms                                                                | 78.0 ms: 1.01x faster                                                        |
| xml_etree_process       | 54.4 ms                                                                | 54.0 ms: 1.01x faster                                                        |
| asyncio_tcp             | 497 ms                                                                 | 494 ms: 1.01x faster                                                         |
| sympy_str               | 272 ms                                                                 | 270 ms: 1.01x faster                                                         |
| scimark_fft             | 303 ms                                                                 | 302 ms: 1.00x faster                                                         |
| 2to3                    | 254 ms                                                                 | 253 ms: 1.00x faster                                                         |
| sqlglot_normalize       | 105 ms                                                                 | 105 ms: 1.00x faster                                                         |
| pickle_pure_python      | 288 us                                                                 | 287 us: 1.00x faster                                                         |
| regex_compile           | 129 ms                                                                 | 128 ms: 1.00x faster                                                         |
| aiohttp                 | 998 us                                                                 | 996 us: 1.00x faster                                                         |
| sympy_sum               | 155 ms                                                                 | 156 ms: 1.00x slower                                                         |
| go                      | 136 ms                                                                 | 137 ms: 1.01x slower                                                         |
| sqlglot_parse           | 1.42 ms                                                                | 1.43 ms: 1.01x slower                                                        |
| json_dumps              | 9.28 ms                                                                | 9.33 ms: 1.01x slower                                                        |
| mdp                     | 2.51 sec                                                               | 2.53 sec: 1.01x slower                                                       |
| mako                    | 9.69 ms                                                                | 9.75 ms: 1.01x slower                                                        |
| generators              | 76.8 ms                                                                | 77.3 ms: 1.01x slower                                                        |
| gunicorn                | 1.07 ms                                                                | 1.08 ms: 1.01x slower                                                        |
| float                   | 72.1 ms                                                                | 72.7 ms: 1.01x slower                                                        |
| deltablue               | 3.22 ms                                                                | 3.25 ms: 1.01x slower                                                        |
| json                    | 4.59 ms                                                                | 4.64 ms: 1.01x slower                                                        |
| docutils                | 2.50 sec                                                               | 2.53 sec: 1.01x slower                                                       |
| pickle                  | 10.0 us                                                                | 10.2 us: 1.02x slower                                                        |
| nbody                   | 92.9 ms                                                                | 94.4 ms: 1.02x slower                                                        |
| regex_effbot            | 3.57 ms                                                                | 3.63 ms: 1.02x slower                                                        |
| unpickle_pure_python    | 198 us                                                                 | 202 us: 1.02x slower                                                         |
| coverage                | 97.8 ms                                                                | 100 ms: 1.03x slower                                                         |
| scimark_sor             | 106 ms                                                                 | 109 ms: 1.03x slower                                                         |
| regex_dna               | 209 ms                                                                 | 217 ms: 1.03x slower                                                         |
| xml_etree_iterparse     | 103 ms                                                                 | 107 ms: 1.04x slower                                                         |
| pidigits                | 189 ms                                                                 | 198 ms: 1.04x slower                                                         |
| pycparser               | 1.10 sec                                                               | 1.15 sec: 1.04x slower                                                       |
| regex_v8                | 21.1 ms                                                                | 22.5 ms: 1.06x slower                                                        |
| pickle_list             | 4.03 us                                                                | 4.31 us: 1.07x slower                                                        |
| pickle_dict             | 29.9 us                                                                | 32.2 us: 1.08x slower                                                        |
| gc_traversal            | 3.91 ms                                                                | 4.27 ms: 1.09x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (27): async_tree_none, scimark_lu, unpickle, thrift, xml_etree_parse, pyflate, chaos, django_template, dulwich_log, logging_silent, deepcopy_memo, sqlglot_transpile, djangocms, unpickle_list, scimark_sparse_mat_mult, async_tree_io, bench_mp_pool, sympy_integrate, pprint_pformat, bench_thread_pool, pprint_safe_repr, tornado_http, json_loads, telco, mypy, dask, html5lib
