
# Results vs. base

- fork: iritkatriel
- ref: single_op_exit
- machine: linux-x86_64
- commit hash: 4684fa7
- commit date: 2023-01-27
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 251 ms: 1.00x slower                                                  |
| chameleon      | 6.29 ms                                                                | 6.53 ms: 1.04x slower                                                 |
| tornado_http   | 94.4 ms                                                                | 93.0 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 193 ms                                                                 | 189 ms: 1.02x faster                                                  |
| float          | 71.9 ms                                                                | 72.8 ms: 1.01x slower                                                 |
| nbody          | 92.9 ms                                                                | 95.1 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 201 ms                                                                 | 209 ms: 1.04x slower                                                  |
| regex_effbot   | 3.38 ms                                                                | 3.57 ms: 1.06x slower                                                 |
| regex_v8       | 21.1 ms                                                                | 25.9 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                                 | 102 ms: 1.05x faster                                                  |
| pickle               | 10.2 us                                                                | 10.1 us: 1.01x faster                                                 |
| unpickle_pure_python | 198 us                                                                 | 197 us: 1.01x faster                                                  |
| unpickle_list        | 5.00 us                                                                | 4.98 us: 1.00x faster                                                 |
| json_dumps           | 9.31 ms                                                                | 9.28 ms: 1.00x faster                                                 |
| pickle_dict          | 31.0 us                                                                | 31.1 us: 1.00x slower                                                 |
| xml_etree_generate   | 77.0 ms                                                                | 77.6 ms: 1.01x slower                                                 |
| xml_etree_process    | 53.5 ms                                                                | 54.1 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_parse, pickle_list, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.95 ms                                                                | 8.96 ms: 1.00x slower                                                 |
| python_startup_no_site | 6.47 ms                                                                | 6.48 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 20.6 ms                                                                | 20.4 ms: 1.01x faster                                                 |
| django_template | 32.8 ms                                                                | 32.5 ms: 1.01x faster                                                 |
| genshi_xml      | 46.4 ms                                                                | 46.1 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse     | 107 ms                                                                 | 102 ms: 1.05x faster                                                  |
| unpack_sequence         | 44.3 ns                                                                | 42.8 ns: 1.03x faster                                                 |
| scimark_monte_carlo     | 65.5 ms                                                                | 64.2 ms: 1.02x faster                                                 |
| coroutines              | 25.4 ms                                                                | 24.8 ms: 1.02x faster                                                 |
| generators              | 76.4 ms                                                                | 74.9 ms: 1.02x faster                                                 |
| pidigits                | 193 ms                                                                 | 189 ms: 1.02x faster                                                  |
| chaos                   | 65.8 ms                                                                | 64.8 ms: 1.02x faster                                                 |
| logging_format          | 6.35 us                                                                | 6.25 us: 1.02x faster                                                 |
| deepcopy_reduce         | 2.97 us                                                                | 2.93 us: 1.01x faster                                                 |
| tornado_http            | 94.4 ms                                                                | 93.0 ms: 1.01x faster                                                 |
| dulwich_log             | 62.6 ms                                                                | 61.8 ms: 1.01x faster                                                 |
| dask                    | 498 ms                                                                 | 491 ms: 1.01x faster                                                  |
| crypto_pyaes            | 74.2 ms                                                                | 73.3 ms: 1.01x faster                                                 |
| coverage                | 98.8 ms                                                                | 97.8 ms: 1.01x faster                                                 |
| genshi_text             | 20.6 ms                                                                | 20.4 ms: 1.01x faster                                                 |
| sympy_expand            | 456 ms                                                                 | 452 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult | 4.03 ms                                                                | 3.99 ms: 1.01x faster                                                 |
| pickle                  | 10.2 us                                                                | 10.1 us: 1.01x faster                                                 |
| django_template         | 32.8 ms                                                                | 32.5 ms: 1.01x faster                                                 |
| bench_thread_pool       | 775 us                                                                 | 769 us: 1.01x faster                                                  |
| sympy_str               | 270 ms                                                                 | 268 ms: 1.01x faster                                                  |
| deepcopy                | 329 us                                                                 | 327 us: 1.01x faster                                                  |
| genshi_xml              | 46.4 ms                                                                | 46.1 ms: 1.01x faster                                                 |
| sympy_sum               | 156 ms                                                                 | 154 ms: 1.01x faster                                                  |
| asyncio_tcp             | 499 ms                                                                 | 496 ms: 1.01x faster                                                  |
| create_gc_cycles        | 1.48 ms                                                                | 1.47 ms: 1.01x faster                                                 |
| raytrace                | 282 ms                                                                 | 281 ms: 1.01x faster                                                  |
| hexiom                  | 5.97 ms                                                                | 5.94 ms: 1.01x faster                                                 |
| unpickle_pure_python    | 198 us                                                                 | 197 us: 1.01x faster                                                  |
| unpickle_list           | 5.00 us                                                                | 4.98 us: 1.00x faster                                                 |
| pprint_pformat          | 1.39 sec                                                               | 1.38 sec: 1.00x faster                                                |
| sqlglot_optimize        | 50.8 ms                                                                | 50.6 ms: 1.00x faster                                                 |
| json_dumps              | 9.31 ms                                                                | 9.28 ms: 1.00x faster                                                 |
| python_startup          | 8.95 ms                                                                | 8.96 ms: 1.00x slower                                                 |
| python_startup_no_site  | 6.47 ms                                                                | 6.48 ms: 1.00x slower                                                 |
| 2to3                    | 250 ms                                                                 | 251 ms: 1.00x slower                                                  |
| pickle_dict             | 31.0 us                                                                | 31.1 us: 1.00x slower                                                 |
| nqueens                 | 76.3 ms                                                                | 76.8 ms: 1.01x slower                                                 |
| pyflate                 | 396 ms                                                                 | 399 ms: 1.01x slower                                                  |
| xml_etree_generate      | 77.0 ms                                                                | 77.6 ms: 1.01x slower                                                 |
| pycparser               | 1.08 sec                                                               | 1.09 sec: 1.01x slower                                                |
| deepcopy_memo           | 34.4 us                                                                | 34.7 us: 1.01x slower                                                 |
| thrift                  | 747 us                                                                 | 755 us: 1.01x slower                                                  |
| xml_etree_process       | 53.5 ms                                                                | 54.1 ms: 1.01x slower                                                 |
| scimark_fft             | 298 ms                                                                 | 301 ms: 1.01x slower                                                  |
| float                   | 71.9 ms                                                                | 72.8 ms: 1.01x slower                                                 |
| async_generators        | 350 ms                                                                 | 354 ms: 1.01x slower                                                  |
| deltablue               | 3.20 ms                                                                | 3.26 ms: 1.02x slower                                                 |
| djangocms               | 32.1 us                                                                | 32.7 us: 1.02x slower                                                 |
| scimark_sor             | 105 ms                                                                 | 107 ms: 1.02x slower                                                  |
| nbody                   | 92.9 ms                                                                | 95.1 ms: 1.02x slower                                                 |
| fannkuch                | 365 ms                                                                 | 377 ms: 1.03x slower                                                  |
| go                      | 132 ms                                                                 | 137 ms: 1.04x slower                                                  |
| chameleon               | 6.29 ms                                                                | 6.53 ms: 1.04x slower                                                 |
| regex_dna               | 201 ms                                                                 | 209 ms: 1.04x slower                                                  |
| mdp                     | 2.57 sec                                                               | 2.69 sec: 1.05x slower                                                |
| regex_effbot            | 3.38 ms                                                                | 3.57 ms: 1.06x slower                                                 |
| gc_traversal            | 3.81 ms                                                                | 4.30 ms: 1.13x slower                                                 |
| regex_v8                | 21.1 ms                                                                | 25.9 ms: 1.23x slower                                                 |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (32): meteor_contest, async_tree_io, spectral_norm, async_tree_none, html5lib, async_tree_cpu_io_mixed, regex_compile, pprint_safe_repr, pickle_pure_python, mypy, gunicorn, xml_etree_parse, pickle_list, docutils, sqlite_synth, mako, logging_simple, json_loads, bench_mp_pool, sympy_integrate, json, telco, pathlib, aiohttp, richards, sqlglot_normalize, sqlglot_parse, sqlglot_transpile, scimark_lu, unpickle, logging_silent, async_tree_memoization
