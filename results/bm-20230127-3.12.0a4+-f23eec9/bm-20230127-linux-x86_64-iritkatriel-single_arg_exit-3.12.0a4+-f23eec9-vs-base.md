
# Results vs. base

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: f23eec9
- commit date: 2023-01-27
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 251 ms: 1.00x slower                                                   |
| tornado_http   | 94.4 ms                                                                | 93.9 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (3): chameleon, docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 92.9 ms                                                                | 94.0 ms: 1.01x slower                                                  |
| pidigits       | 193 ms                                                                 | 198 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 201 ms                                                                 | 210 ms: 1.04x slower                                                   |
| regex_effbot   | 3.38 ms                                                                | 3.57 ms: 1.06x slower                                                  |
| regex_v8       | 21.1 ms                                                                | 26.0 ms: 1.23x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.08x slower                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_list         | 4.22 us                                                                | 4.03 us: 1.05x faster                                                  |
| xml_etree_iterparse | 107 ms                                                                 | 102 ms: 1.04x faster                                                   |
| pickle              | 10.2 us                                                                | 10.1 us: 1.01x faster                                                  |
| pickle_pure_python  | 284 us                                                                 | 282 us: 1.01x faster                                                   |
| pickle_dict         | 31.0 us                                                                | 30.8 us: 1.00x faster                                                  |
| json_loads          | 24.1 us                                                                | 24.0 us: 1.00x faster                                                  |
| xml_etree_generate  | 77.0 ms                                                                | 77.3 ms: 1.00x slower                                                  |
| json_dumps          | 9.31 ms                                                                | 9.38 ms: 1.01x slower                                                  |
| unpickle_list       | 5.00 us                                                                | 5.04 us: 1.01x slower                                                  |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.95 ms                                                                | 8.90 ms: 1.01x faster                                                  |
| python_startup_no_site | 6.47 ms                                                                | 6.45 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, mako, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark              | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_list            | 4.22 us                                                                | 4.03 us: 1.05x faster                                                  |
| xml_etree_iterparse    | 107 ms                                                                 | 102 ms: 1.04x faster                                                   |
| coroutines             | 25.4 ms                                                                | 24.5 ms: 1.04x faster                                                  |
| logging_format         | 6.35 us                                                                | 6.19 us: 1.02x faster                                                  |
| meteor_contest         | 106 ms                                                                 | 104 ms: 1.02x faster                                                   |
| coverage               | 98.8 ms                                                                | 97.2 ms: 1.02x faster                                                  |
| logging_simple         | 5.71 us                                                                | 5.62 us: 1.02x faster                                                  |
| crypto_pyaes           | 74.2 ms                                                                | 73.0 ms: 1.02x faster                                                  |
| create_gc_cycles       | 1.48 ms                                                                | 1.46 ms: 1.01x faster                                                  |
| chaos                  | 65.8 ms                                                                | 64.9 ms: 1.01x faster                                                  |
| pickle                 | 10.2 us                                                                | 10.1 us: 1.01x faster                                                  |
| json                   | 4.61 ms                                                                | 4.56 ms: 1.01x faster                                                  |
| sympy_expand           | 456 ms                                                                 | 453 ms: 1.01x faster                                                   |
| unpack_sequence        | 44.3 ns                                                                | 44.0 ns: 1.01x faster                                                  |
| fannkuch               | 365 ms                                                                 | 363 ms: 1.01x faster                                                   |
| python_startup         | 8.95 ms                                                                | 8.90 ms: 1.01x faster                                                  |
| tornado_http           | 94.4 ms                                                                | 93.9 ms: 1.01x faster                                                  |
| pathlib                | 17.8 ms                                                                | 17.7 ms: 1.01x faster                                                  |
| pickle_pure_python     | 284 us                                                                 | 282 us: 1.01x faster                                                   |
| pickle_dict            | 31.0 us                                                                | 30.8 us: 1.00x faster                                                  |
| json_loads             | 24.1 us                                                                | 24.0 us: 1.00x faster                                                  |
| asyncio_tcp            | 499 ms                                                                 | 498 ms: 1.00x faster                                                   |
| python_startup_no_site | 6.47 ms                                                                | 6.45 ms: 1.00x faster                                                  |
| sympy_integrate        | 19.7 ms                                                                | 19.7 ms: 1.00x slower                                                  |
| aiohttp                | 991 us                                                                 | 995 us: 1.00x slower                                                   |
| xml_etree_generate     | 77.0 ms                                                                | 77.3 ms: 1.00x slower                                                  |
| 2to3                   | 250 ms                                                                 | 251 ms: 1.00x slower                                                   |
| gunicorn               | 1.06 ms                                                                | 1.06 ms: 1.01x slower                                                  |
| hexiom                 | 5.97 ms                                                                | 6.00 ms: 1.01x slower                                                  |
| sqlglot_normalize      | 104 ms                                                                 | 105 ms: 1.01x slower                                                   |
| pyflate                | 396 ms                                                                 | 399 ms: 1.01x slower                                                   |
| async_generators       | 350 ms                                                                 | 352 ms: 1.01x slower                                                   |
| json_dumps             | 9.31 ms                                                                | 9.38 ms: 1.01x slower                                                  |
| unpickle_list          | 5.00 us                                                                | 5.04 us: 1.01x slower                                                  |
| sqlglot_optimize       | 50.8 ms                                                                | 51.3 ms: 1.01x slower                                                  |
| deepcopy_memo          | 34.4 us                                                                | 34.8 us: 1.01x slower                                                  |
| nbody                  | 92.9 ms                                                                | 94.0 ms: 1.01x slower                                                  |
| richards               | 42.0 ms                                                                | 42.5 ms: 1.01x slower                                                  |
| deepcopy               | 329 us                                                                 | 334 us: 1.01x slower                                                   |
| scimark_lu             | 106 ms                                                                 | 107 ms: 1.01x slower                                                   |
| generators             | 76.4 ms                                                                | 77.4 ms: 1.01x slower                                                  |
| telco                  | 6.28 ms                                                                | 6.39 ms: 1.02x slower                                                  |
| scimark_fft            | 298 ms                                                                 | 303 ms: 1.02x slower                                                   |
| djangocms              | 32.1 us                                                                | 32.8 us: 1.02x slower                                                  |
| pidigits               | 193 ms                                                                 | 198 ms: 1.03x slower                                                   |
| async_tree_memoization | 627 ms                                                                 | 645 ms: 1.03x slower                                                   |
| spectral_norm          | 97.0 ms                                                                | 100 ms: 1.03x slower                                                   |
| go                     | 132 ms                                                                 | 137 ms: 1.04x slower                                                   |
| logging_silent         | 91.3 ns                                                                | 94.9 ns: 1.04x slower                                                  |
| regex_dna              | 201 ms                                                                 | 210 ms: 1.04x slower                                                   |
| pycparser              | 1.08 sec                                                               | 1.14 sec: 1.05x slower                                                 |
| regex_effbot           | 3.38 ms                                                                | 3.57 ms: 1.06x slower                                                  |
| gc_traversal           | 3.81 ms                                                                | 4.29 ms: 1.13x slower                                                  |
| regex_v8               | 21.1 ms                                                                | 26.0 ms: 1.23x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (37): unpickle, dask, async_tree_none, html5lib, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, sympy_str, raytrace, xml_etree_parse, float, docutils, async_tree_io, pprint_pformat, sympy_sum, chameleon, mdp, dulwich_log, bench_mp_pool, nqueens, django_template, unpickle_pure_python, sqlglot_transpile, mako, sqlglot_parse, bench_thread_pool, mypy, genshi_xml, deepcopy_reduce, pprint_safe_repr, xml_etree_process, sqlite_synth, deltablue, thrift, scimark_sor, regex_compile, scimark_monte_carlo, genshi_text
