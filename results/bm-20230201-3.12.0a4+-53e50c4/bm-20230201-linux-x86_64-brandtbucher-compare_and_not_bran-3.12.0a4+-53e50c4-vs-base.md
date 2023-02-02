
# Results vs. base

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 53e50c4
- commit date: 2023-02-01
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 254 ms: 1.00x faster                                                         |
| docutils       | 2.51 sec                                                               | 2.55 sec: 1.01x slower                                                       |
| tornado_http   | 94.9 ms                                                                | 94.1 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 95.3 ms                                                                | 93.7 ms: 1.02x faster                                                        |
| pidigits       | 189 ms                                                                 | 190 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                 | 210 ms: 1.05x faster                                                         |
| regex_effbot   | 3.61 ms                                                                | 3.52 ms: 1.03x faster                                                        |
| regex_v8       | 22.6 ms                                                                | 22.2 ms: 1.02x faster                                                        |
| regex_compile  | 129 ms                                                                 | 130 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_list        | 5.10 us                                                                | 4.96 us: 1.03x faster                                                        |
| unpickle             | 13.3 us                                                                | 13.0 us: 1.03x faster                                                        |
| xml_etree_generate   | 77.3 ms                                                                | 77.7 ms: 1.01x slower                                                        |
| pickle_pure_python   | 285 us                                                                 | 288 us: 1.01x slower                                                         |
| json_dumps           | 9.42 ms                                                                | 9.62 ms: 1.02x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                                 | 105 ms: 1.02x slower                                                         |
| pickle_dict          | 29.9 us                                                                | 30.7 us: 1.03x slower                                                        |
| pickle_list          | 3.98 us                                                                | 4.10 us: 1.03x slower                                                        |
| unpickle_pure_python | 197 us                                                                 | 202 us: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): json_loads, xml_etree_process, xml_etree_parse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.49 ms                                                                | 6.44 ms: 1.01x faster                                                        |
| python_startup         | 8.96 ms                                                                | 8.89 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 20.9 ms                                                                | 20.4 ms: 1.02x faster                                                        |
| django_template | 32.5 ms                                                                | 32.3 ms: 1.01x faster                                                        |
| mako            | 9.53 ms                                                                | 9.69 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna               | 219 ms                                                                 | 210 ms: 1.05x faster                                                         |
| unpickle_list           | 5.10 us                                                                | 4.96 us: 1.03x faster                                                        |
| unpickle                | 13.3 us                                                                | 13.0 us: 1.03x faster                                                        |
| regex_effbot            | 3.61 ms                                                                | 3.52 ms: 1.03x faster                                                        |
| scimark_lu              | 108 ms                                                                 | 105 ms: 1.02x faster                                                         |
| genshi_text             | 20.9 ms                                                                | 20.4 ms: 1.02x faster                                                        |
| regex_v8                | 22.6 ms                                                                | 22.2 ms: 1.02x faster                                                        |
| raytrace                | 286 ms                                                                 | 281 ms: 1.02x faster                                                         |
| scimark_fft             | 308 ms                                                                 | 302 ms: 1.02x faster                                                         |
| meteor_contest          | 106 ms                                                                 | 104 ms: 1.02x faster                                                         |
| nbody                   | 95.3 ms                                                                | 93.7 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult | 4.06 ms                                                                | 4.00 ms: 1.02x faster                                                        |
| fannkuch                | 369 ms                                                                 | 364 ms: 1.02x faster                                                         |
| coroutines              | 25.9 ms                                                                | 25.5 ms: 1.01x faster                                                        |
| spectral_norm           | 95.7 ms                                                                | 94.5 ms: 1.01x faster                                                        |
| hexiom                  | 5.96 ms                                                                | 5.89 ms: 1.01x faster                                                        |
| sqlglot_optimize        | 51.6 ms                                                                | 51.0 ms: 1.01x faster                                                        |
| deltablue               | 3.25 ms                                                                | 3.21 ms: 1.01x faster                                                        |
| sympy_expand            | 459 ms                                                                 | 454 ms: 1.01x faster                                                         |
| dask                    | 503 ms                                                                 | 497 ms: 1.01x faster                                                         |
| pyflate                 | 404 ms                                                                 | 400 ms: 1.01x faster                                                         |
| pycparser               | 1.16 sec                                                               | 1.15 sec: 1.01x faster                                                       |
| sqlglot_transpile       | 1.72 ms                                                                | 1.71 ms: 1.01x faster                                                        |
| tornado_http            | 94.9 ms                                                                | 94.1 ms: 1.01x faster                                                        |
| scimark_monte_carlo     | 65.5 ms                                                                | 65.0 ms: 1.01x faster                                                        |
| python_startup_no_site  | 6.49 ms                                                                | 6.44 ms: 1.01x faster                                                        |
| sqlglot_parse           | 1.43 ms                                                                | 1.42 ms: 1.01x faster                                                        |
| python_startup          | 8.96 ms                                                                | 8.89 ms: 1.01x faster                                                        |
| django_template         | 32.5 ms                                                                | 32.3 ms: 1.01x faster                                                        |
| sqlglot_normalize       | 106 ms                                                                 | 106 ms: 1.01x faster                                                         |
| deepcopy                | 331 us                                                                 | 329 us: 1.01x faster                                                         |
| sympy_sum               | 156 ms                                                                 | 155 ms: 1.01x faster                                                         |
| sympy_integrate         | 19.8 ms                                                                | 19.7 ms: 1.00x faster                                                        |
| gunicorn                | 1.07 ms                                                                | 1.07 ms: 1.00x faster                                                        |
| generators              | 76.9 ms                                                                | 76.5 ms: 1.00x faster                                                        |
| pprint_pformat          | 1.38 sec                                                               | 1.38 sec: 1.00x faster                                                       |
| aiohttp                 | 998 us                                                                 | 995 us: 1.00x faster                                                         |
| create_gc_cycles        | 1.46 ms                                                                | 1.46 ms: 1.00x faster                                                        |
| 2to3                    | 254 ms                                                                 | 254 ms: 1.00x faster                                                         |
| bench_mp_pool           | 24.0 ms                                                                | 24.0 ms: 1.00x faster                                                        |
| pidigits                | 189 ms                                                                 | 190 ms: 1.00x slower                                                         |
| crypto_pyaes            | 72.6 ms                                                                | 72.9 ms: 1.00x slower                                                        |
| xml_etree_generate      | 77.3 ms                                                                | 77.7 ms: 1.01x slower                                                        |
| bench_thread_pool       | 782 us                                                                 | 787 us: 1.01x slower                                                         |
| pprint_safe_repr        | 671 ms                                                                 | 675 ms: 1.01x slower                                                         |
| asyncio_tcp             | 497 ms                                                                 | 500 ms: 1.01x slower                                                         |
| async_generators        | 351 ms                                                                 | 353 ms: 1.01x slower                                                         |
| logging_simple          | 5.75 us                                                                | 5.78 us: 1.01x slower                                                        |
| async_tree_io           | 1.32 sec                                                               | 1.33 sec: 1.01x slower                                                       |
| coverage                | 95.2 ms                                                                | 96.1 ms: 1.01x slower                                                        |
| deepcopy_memo           | 34.3 us                                                                | 34.7 us: 1.01x slower                                                        |
| pickle_pure_python      | 285 us                                                                 | 288 us: 1.01x slower                                                         |
| go                      | 135 ms                                                                 | 137 ms: 1.01x slower                                                         |
| regex_compile           | 129 ms                                                                 | 130 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed | 750 ms                                                                 | 759 ms: 1.01x slower                                                         |
| docutils                | 2.51 sec                                                               | 2.55 sec: 1.01x slower                                                       |
| deepcopy_reduce         | 2.89 us                                                                | 2.93 us: 1.01x slower                                                        |
| mako                    | 9.53 ms                                                                | 9.69 ms: 1.02x slower                                                        |
| json                    | 4.62 ms                                                                | 4.70 ms: 1.02x slower                                                        |
| chaos                   | 63.8 ms                                                                | 65.0 ms: 1.02x slower                                                        |
| json_dumps              | 9.42 ms                                                                | 9.62 ms: 1.02x slower                                                        |
| xml_etree_iterparse     | 103 ms                                                                 | 105 ms: 1.02x slower                                                         |
| mdp                     | 2.51 sec                                                               | 2.58 sec: 1.03x slower                                                       |
| pickle_dict             | 29.9 us                                                                | 30.7 us: 1.03x slower                                                        |
| scimark_sor             | 105 ms                                                                 | 108 ms: 1.03x slower                                                         |
| pickle_list             | 3.98 us                                                                | 4.10 us: 1.03x slower                                                        |
| unpickle_pure_python    | 197 us                                                                 | 202 us: 1.03x slower                                                         |
| unpack_sequence         | 42.1 ns                                                                | 43.6 ns: 1.03x slower                                                        |
| nqueens                 | 75.0 ms                                                                | 79.0 ms: 1.05x slower                                                        |
| gc_traversal            | 3.65 ms                                                                | 4.05 ms: 1.11x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (21): richards, telco, djangocms, sympy_str, thrift, json_loads, float, mypy, logging_format, dulwich_log, sqlite_synth, genshi_xml, pathlib, xml_etree_process, chameleon, xml_etree_parse, pickle, logging_silent, async_tree_memoization, async_tree_none, html5lib
