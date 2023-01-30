
# Results vs. base

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: 00b5a0c
- commit date: 2023-01-27
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 254 ms: 1.02x slower                                                   |
| chameleon      | 6.29 ms                                                                | 6.42 ms: 1.02x slower                                                  |
| docutils       | 2.50 sec                                                               | 2.51 sec: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 193 ms                                                                 | 189 ms: 1.02x faster                                                   |
| float          | 71.9 ms                                                                | 72.5 ms: 1.01x slower                                                  |
| nbody          | 92.9 ms                                                                | 94.8 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 21.1 ms                                                                | 21.5 ms: 1.02x slower                                                  |
| regex_dna      | 201 ms                                                                 | 205 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                                 | 102 ms: 1.04x faster                                                   |
| unpickle             | 13.2 us                                                                | 13.0 us: 1.02x faster                                                  |
| pickle_list          | 4.22 us                                                                | 4.15 us: 1.02x faster                                                  |
| unpickle_list        | 5.00 us                                                                | 4.95 us: 1.01x faster                                                  |
| xml_etree_parse      | 147 ms                                                                 | 146 ms: 1.01x faster                                                   |
| pickle_pure_python   | 284 us                                                                 | 285 us: 1.00x slower                                                   |
| xml_etree_generate   | 77.0 ms                                                                | 77.8 ms: 1.01x slower                                                  |
| pickle_dict          | 31.0 us                                                                | 31.3 us: 1.01x slower                                                  |
| unpickle_pure_python | 198 us                                                                 | 201 us: 1.01x slower                                                   |
| json_loads           | 24.1 us                                                                | 25.7 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (3): xml_etree_process, pickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.95 ms                                                                | 8.96 ms: 1.00x slower                                                  |
| python_startup_no_site | 6.47 ms                                                                | 6.54 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.70 ms                                                                | 9.45 ms: 1.03x faster                                                  |
| genshi_text     | 20.6 ms                                                                | 20.4 ms: 1.01x faster                                                  |
| genshi_xml      | 46.4 ms                                                                | 46.7 ms: 1.01x slower                                                  |
| django_template | 32.8 ms                                                                | 33.3 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mypy                    | 805 ms                                                                 | 647 ms: 1.24x faster                                                   |
| gc_traversal            | 3.81 ms                                                                | 3.41 ms: 1.12x faster                                                  |
| xml_etree_iterparse     | 107 ms                                                                 | 102 ms: 1.04x faster                                                   |
| mdp                     | 2.57 sec                                                               | 2.47 sec: 1.04x faster                                                 |
| mako                    | 9.70 ms                                                                | 9.45 ms: 1.03x faster                                                  |
| async_tree_none         | 528 ms                                                                 | 517 ms: 1.02x faster                                                   |
| unpickle                | 13.2 us                                                                | 13.0 us: 1.02x faster                                                  |
| deepcopy_memo           | 34.4 us                                                                | 33.8 us: 1.02x faster                                                  |
| deepcopy_reduce         | 2.97 us                                                                | 2.92 us: 1.02x faster                                                  |
| async_tree_cpu_io_mixed | 760 ms                                                                 | 747 ms: 1.02x faster                                                   |
| pickle_list             | 4.22 us                                                                | 4.15 us: 1.02x faster                                                  |
| pidigits                | 193 ms                                                                 | 189 ms: 1.02x faster                                                   |
| spectral_norm           | 97.0 ms                                                                | 95.4 ms: 1.02x faster                                                  |
| crypto_pyaes            | 74.2 ms                                                                | 73.1 ms: 1.02x faster                                                  |
| meteor_contest          | 106 ms                                                                 | 105 ms: 1.01x faster                                                   |
| unpack_sequence         | 44.3 ns                                                                | 43.8 ns: 1.01x faster                                                  |
| unpickle_list           | 5.00 us                                                                | 4.95 us: 1.01x faster                                                  |
| genshi_text             | 20.6 ms                                                                | 20.4 ms: 1.01x faster                                                  |
| pprint_pformat          | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                                 |
| pprint_safe_repr        | 676 ms                                                                 | 671 ms: 1.01x faster                                                   |
| xml_etree_parse         | 147 ms                                                                 | 146 ms: 1.01x faster                                                   |
| pyflate                 | 396 ms                                                                 | 394 ms: 1.01x faster                                                   |
| python_startup          | 8.95 ms                                                                | 8.96 ms: 1.00x slower                                                  |
| docutils                | 2.50 sec                                                               | 2.51 sec: 1.00x slower                                                 |
| pickle_pure_python      | 284 us                                                                 | 285 us: 1.00x slower                                                   |
| async_generators        | 350 ms                                                                 | 352 ms: 1.01x slower                                                   |
| genshi_xml              | 46.4 ms                                                                | 46.7 ms: 1.01x slower                                                  |
| logging_silent          | 91.3 ns                                                                | 92.0 ns: 1.01x slower                                                  |
| sympy_str               | 270 ms                                                                 | 273 ms: 1.01x slower                                                   |
| float                   | 71.9 ms                                                                | 72.5 ms: 1.01x slower                                                  |
| richards                | 42.0 ms                                                                | 42.4 ms: 1.01x slower                                                  |
| python_startup_no_site  | 6.47 ms                                                                | 6.54 ms: 1.01x slower                                                  |
| pathlib                 | 17.8 ms                                                                | 18.0 ms: 1.01x slower                                                  |
| sympy_expand            | 456 ms                                                                 | 461 ms: 1.01x slower                                                   |
| xml_etree_generate      | 77.0 ms                                                                | 77.8 ms: 1.01x slower                                                  |
| pickle_dict             | 31.0 us                                                                | 31.3 us: 1.01x slower                                                  |
| sympy_integrate         | 19.7 ms                                                                | 20.0 ms: 1.01x slower                                                  |
| unpickle_pure_python    | 198 us                                                                 | 201 us: 1.01x slower                                                   |
| deltablue               | 3.20 ms                                                                | 3.25 ms: 1.01x slower                                                  |
| django_template         | 32.8 ms                                                                | 33.3 ms: 1.01x slower                                                  |
| 2to3                    | 250 ms                                                                 | 254 ms: 1.02x slower                                                   |
| logging_format          | 6.35 us                                                                | 6.45 us: 1.02x slower                                                  |
| regex_v8                | 21.1 ms                                                                | 21.5 ms: 1.02x slower                                                  |
| scimark_sor             | 105 ms                                                                 | 107 ms: 1.02x slower                                                   |
| nbody                   | 92.9 ms                                                                | 94.8 ms: 1.02x slower                                                  |
| regex_dna               | 201 ms                                                                 | 205 ms: 1.02x slower                                                   |
| chameleon               | 6.29 ms                                                                | 6.42 ms: 1.02x slower                                                  |
| chaos                   | 65.8 ms                                                                | 67.2 ms: 1.02x slower                                                  |
| scimark_monte_carlo     | 65.5 ms                                                                | 67.1 ms: 1.02x slower                                                  |
| sqlglot_optimize        | 50.8 ms                                                                | 52.1 ms: 1.03x slower                                                  |
| generators              | 76.4 ms                                                                | 78.4 ms: 1.03x slower                                                  |
| logging_simple          | 5.71 us                                                                | 5.87 us: 1.03x slower                                                  |
| aiohttp                 | 991 us                                                                 | 1.02 ms: 1.03x slower                                                  |
| async_tree_memoization  | 627 ms                                                                 | 646 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult | 4.03 ms                                                                | 4.17 ms: 1.03x slower                                                  |
| sqlglot_normalize       | 104 ms                                                                 | 108 ms: 1.03x slower                                                   |
| pycparser               | 1.08 sec                                                               | 1.12 sec: 1.04x slower                                                 |
| json                    | 4.61 ms                                                                | 4.78 ms: 1.04x slower                                                  |
| dask                    | 498 ms                                                                 | 518 ms: 1.04x slower                                                   |
| gunicorn                | 1.06 ms                                                                | 1.10 ms: 1.04x slower                                                  |
| djangocms               | 32.1 us                                                                | 33.5 us: 1.04x slower                                                  |
| fannkuch                | 365 ms                                                                 | 381 ms: 1.05x slower                                                   |
| scimark_fft             | 298 ms                                                                 | 311 ms: 1.05x slower                                                   |
| go                      | 132 ms                                                                 | 138 ms: 1.05x slower                                                   |
| scimark_lu              | 106 ms                                                                 | 112 ms: 1.06x slower                                                   |
| json_loads              | 24.1 us                                                                | 25.7 us: 1.07x slower                                                  |
| create_gc_cycles        | 1.48 ms                                                                | 1.66 ms: 1.12x slower                                                  |
| bench_thread_pool       | 775 us                                                                 | 963 us: 1.24x slower                                                   |
| bench_mp_pool           | 24.0 ms                                                                | 30.6 ms: 1.27x slower                                                  |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (22): coroutines, telco, async_tree_io, asyncio_tcp, regex_effbot, xml_etree_process, nqueens, pickle, deepcopy, json_dumps, sympy_sum, hexiom, sqlglot_parse, regex_compile, dulwich_log, thrift, raytrace, html5lib, tornado_http, sqlglot_transpile, sqlite_synth, coverage
