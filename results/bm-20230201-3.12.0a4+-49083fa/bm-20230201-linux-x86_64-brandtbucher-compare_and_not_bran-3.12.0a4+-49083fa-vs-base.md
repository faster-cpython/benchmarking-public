
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
| chameleon      | 6.59 ms                                                                | 6.50 ms: 1.01x faster                                                        |
| docutils       | 2.50 sec                                                               | 2.53 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 72.1 ms                                                                | 73.8 ms: 1.02x slower                                                        |
| pidigits       | 189 ms                                                                 | 198 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                                | 3.54 ms: 1.01x faster                                                        |
| regex_compile  | 129 ms                                                                 | 134 ms: 1.04x slower                                                         |
| regex_v8       | 21.1 ms                                                                | 22.6 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_process    | 54.4 ms                                                                | 53.5 ms: 1.02x faster                                                        |
| xml_etree_generate   | 78.5 ms                                                                | 77.5 ms: 1.01x faster                                                        |
| unpickle_list        | 5.03 us                                                                | 4.97 us: 1.01x faster                                                        |
| pickle_pure_python   | 288 us                                                                 | 290 us: 1.01x slower                                                         |
| json_dumps           | 9.28 ms                                                                | 9.41 ms: 1.01x slower                                                        |
| unpickle             | 13.1 us                                                                | 13.3 us: 1.02x slower                                                        |
| json_loads           | 23.8 us                                                                | 24.3 us: 1.02x slower                                                        |
| pickle               | 10.0 us                                                                | 10.3 us: 1.03x slower                                                        |
| xml_etree_parse      | 148 ms                                                                 | 151 ms: 1.03x slower                                                         |
| unpickle_pure_python | 198 us                                                                 | 203 us: 1.03x slower                                                         |
| xml_etree_iterparse  | 103 ms                                                                 | 106 ms: 1.04x slower                                                         |
| pickle_list          | 4.03 us                                                                | 4.26 us: 1.06x slower                                                        |
| pickle_dict          | 29.9 us                                                                | 32.1 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.48 ms                                                                | 6.46 ms: 1.00x faster                                                        |
| python_startup         | 8.95 ms                                                                | 8.94 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                                        |
| mako            | 9.69 ms                                                                | 9.78 ms: 1.01x slower                                                        |
| genshi_xml      | 46.6 ms                                                                | 47.5 ms: 1.02x slower                                                        |
| django_template | 32.7 ms                                                                | 33.4 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20230202-linux-x86_64-python-0675b8f032c69d265468-3.12.0a4+-0675b8f | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpack_sequence         | 46.8 ns                                                                | 42.0 ns: 1.11x faster                                                        |
| fannkuch                | 389 ms                                                                 | 364 ms: 1.07x faster                                                         |
| coroutines              | 26.7 ms                                                                | 25.3 ms: 1.05x faster                                                        |
| meteor_contest          | 108 ms                                                                 | 104 ms: 1.05x faster                                                         |
| async_tree_memoization  | 667 ms                                                                 | 642 ms: 1.04x faster                                                         |
| crypto_pyaes            | 74.6 ms                                                                | 72.8 ms: 1.02x faster                                                        |
| hexiom                  | 6.03 ms                                                                | 5.89 ms: 1.02x faster                                                        |
| async_tree_io           | 1.33 sec                                                               | 1.31 sec: 1.02x faster                                                       |
| raytrace                | 287 ms                                                                 | 281 ms: 1.02x faster                                                         |
| generators              | 76.8 ms                                                                | 75.4 ms: 1.02x faster                                                        |
| xml_etree_process       | 54.4 ms                                                                | 53.5 ms: 1.02x faster                                                        |
| async_generators        | 357 ms                                                                 | 351 ms: 1.02x faster                                                         |
| nqueens                 | 77.8 ms                                                                | 76.6 ms: 1.02x faster                                                        |
| asyncio_tcp             | 497 ms                                                                 | 490 ms: 1.02x faster                                                         |
| chameleon               | 6.59 ms                                                                | 6.50 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed | 761 ms                                                                 | 750 ms: 1.01x faster                                                         |
| xml_etree_generate      | 78.5 ms                                                                | 77.5 ms: 1.01x faster                                                        |
| sqlite_synth            | 2.61 us                                                                | 2.58 us: 1.01x faster                                                        |
| sqlglot_optimize        | 51.5 ms                                                                | 50.8 ms: 1.01x faster                                                        |
| unpickle_list           | 5.03 us                                                                | 4.97 us: 1.01x faster                                                        |
| sqlglot_normalize       | 105 ms                                                                 | 104 ms: 1.01x faster                                                         |
| genshi_text             | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                                        |
| sympy_str               | 272 ms                                                                 | 269 ms: 1.01x faster                                                         |
| regex_effbot            | 3.57 ms                                                                | 3.54 ms: 1.01x faster                                                        |
| dulwich_log             | 63.0 ms                                                                | 62.4 ms: 1.01x faster                                                        |
| create_gc_cycles        | 1.48 ms                                                                | 1.46 ms: 1.01x faster                                                        |
| thrift                  | 762 us                                                                 | 756 us: 1.01x faster                                                         |
| sympy_expand            | 457 ms                                                                 | 454 ms: 1.01x faster                                                         |
| logging_simple          | 5.84 us                                                                | 5.80 us: 1.01x faster                                                        |
| 2to3                    | 254 ms                                                                 | 253 ms: 1.00x faster                                                         |
| python_startup_no_site  | 6.48 ms                                                                | 6.46 ms: 1.00x faster                                                        |
| python_startup          | 8.95 ms                                                                | 8.94 ms: 1.00x faster                                                        |
| scimark_fft             | 303 ms                                                                 | 305 ms: 1.00x slower                                                         |
| gunicorn                | 1.07 ms                                                                | 1.07 ms: 1.01x slower                                                        |
| coverage                | 97.8 ms                                                                | 98.3 ms: 1.01x slower                                                        |
| pathlib                 | 17.9 ms                                                                | 18.0 ms: 1.01x slower                                                        |
| pickle_pure_python      | 288 us                                                                 | 290 us: 1.01x slower                                                         |
| pyflate                 | 403 ms                                                                 | 407 ms: 1.01x slower                                                         |
| sqlglot_transpile       | 1.72 ms                                                                | 1.73 ms: 1.01x slower                                                        |
| mako                    | 9.69 ms                                                                | 9.78 ms: 1.01x slower                                                        |
| docutils                | 2.50 sec                                                               | 2.53 sec: 1.01x slower                                                       |
| pprint_safe_repr        | 673 ms                                                                 | 681 ms: 1.01x slower                                                         |
| json_dumps              | 9.28 ms                                                                | 9.41 ms: 1.01x slower                                                        |
| telco                   | 6.42 ms                                                                | 6.52 ms: 1.02x slower                                                        |
| sqlglot_parse           | 1.42 ms                                                                | 1.44 ms: 1.02x slower                                                        |
| go                      | 136 ms                                                                 | 139 ms: 1.02x slower                                                         |
| genshi_xml              | 46.6 ms                                                                | 47.5 ms: 1.02x slower                                                        |
| chaos                   | 64.9 ms                                                                | 66.1 ms: 1.02x slower                                                        |
| pprint_pformat          | 1.38 sec                                                               | 1.41 sec: 1.02x slower                                                       |
| deltablue               | 3.22 ms                                                                | 3.28 ms: 1.02x slower                                                        |
| unpickle                | 13.1 us                                                                | 13.3 us: 1.02x slower                                                        |
| json_loads              | 23.8 us                                                                | 24.3 us: 1.02x slower                                                        |
| deepcopy_memo           | 34.2 us                                                                | 34.9 us: 1.02x slower                                                        |
| richards                | 42.2 ms                                                                | 43.0 ms: 1.02x slower                                                        |
| django_template         | 32.7 ms                                                                | 33.4 ms: 1.02x slower                                                        |
| json                    | 4.59 ms                                                                | 4.69 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult | 3.98 ms                                                                | 4.07 ms: 1.02x slower                                                        |
| float                   | 72.1 ms                                                                | 73.8 ms: 1.02x slower                                                        |
| pickle                  | 10.0 us                                                                | 10.3 us: 1.03x slower                                                        |
| xml_etree_parse         | 148 ms                                                                 | 151 ms: 1.03x slower                                                         |
| unpickle_pure_python    | 198 us                                                                 | 203 us: 1.03x slower                                                         |
| logging_silent          | 92.8 ns                                                                | 95.5 ns: 1.03x slower                                                        |
| scimark_sor             | 106 ms                                                                 | 109 ms: 1.03x slower                                                         |
| xml_etree_iterparse     | 103 ms                                                                 | 106 ms: 1.04x slower                                                         |
| regex_compile           | 129 ms                                                                 | 134 ms: 1.04x slower                                                         |
| pidigits                | 189 ms                                                                 | 198 ms: 1.04x slower                                                         |
| pycparser               | 1.10 sec                                                               | 1.16 sec: 1.05x slower                                                       |
| pickle_list             | 4.03 us                                                                | 4.26 us: 1.06x slower                                                        |
| gc_traversal            | 3.91 ms                                                                | 4.15 ms: 1.06x slower                                                        |
| mdp                     | 2.51 sec                                                               | 2.68 sec: 1.07x slower                                                       |
| regex_v8                | 21.1 ms                                                                | 22.6 ms: 1.07x slower                                                        |
| pickle_dict             | 29.9 us                                                                | 32.1 us: 1.08x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (19): djangocms, async_tree_none, deepcopy_reduce, logging_format, aiohttp, sympy_sum, bench_thread_pool, tornado_http, bench_mp_pool, spectral_norm, regex_dna, scimark_monte_carlo, scimark_lu, sympy_integrate, mypy, dask, deepcopy, nbody, html5lib
