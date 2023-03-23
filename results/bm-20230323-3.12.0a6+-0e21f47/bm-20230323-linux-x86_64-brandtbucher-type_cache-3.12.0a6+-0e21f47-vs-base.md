
# Results vs. base

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: 0e21f47
- commit date: 2023-03-23
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 253 ms: 1.01x slower                                               |
| chameleon      | 6.45 ms                                                                | 6.63 ms: 1.03x slower                                              |
| docutils       | 2.54 sec                                                               | 2.57 sec: 1.01x slower                                             |
| html5lib       | 61.1 ms                                                                | 62.4 ms: 1.02x slower                                              |
| tornado_http   | 91.1 ms                                                                | 92.3 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 88.6 ms                                                                | 86.8 ms: 1.02x faster                                              |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                                | 3.57 ms: 1.01x faster                                              |
| regex_compile  | 135 ms                                                                 | 134 ms: 1.01x faster                                               |
| regex_dna      | 209 ms                                                                 | 208 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse     | 150 ms                                                                 | 148 ms: 1.01x faster                                               |
| xml_etree_generate  | 81.7 ms                                                                | 82.1 ms: 1.00x slower                                              |
| pickle              | 10.4 us                                                                | 10.4 us: 1.01x slower                                              |
| pickle_dict         | 30.5 us                                                                | 30.7 us: 1.01x slower                                              |
| xml_etree_iterparse | 99.2 ms                                                                | 101 ms: 1.01x slower                                               |
| json_dumps          | 9.57 ms                                                                | 9.71 ms: 1.01x slower                                              |
| pickle_pure_python  | 287 us                                                                 | 292 us: 1.02x slower                                               |
| json_loads          | 23.8 us                                                                | 24.2 us: 1.02x slower                                              |
| xml_etree_process   | 56.8 ms                                                                | 58.0 ms: 1.02x slower                                              |
| pickle_list         | 4.24 us                                                                | 4.33 us: 1.02x slower                                              |
| unpickle            | 13.3 us                                                                | 13.8 us: 1.03x slower                                              |
| unpickle_list       | 4.98 us                                                                | 5.28 us: 1.06x slower                                              |
| Geometric mean      | (ref)                                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.55 ms: 1.01x slower                                              |
| python_startup         | 8.79 ms                                                                | 8.87 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 33.8 ms                                                                | 34.0 ms: 1.01x slower                                              |
| genshi_text     | 21.8 ms                                                                | 22.0 ms: 1.01x slower                                              |
| genshi_xml      | 48.1 ms                                                                | 48.9 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark              | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| scimark_fft            | 319 ms                                                                 | 306 ms: 1.04x faster                                               |
| mdp                    | 2.71 sec                                                               | 2.64 sec: 1.03x faster                                             |
| nbody                  | 88.6 ms                                                                | 86.8 ms: 1.02x faster                                              |
| telco                  | 6.52 ms                                                                | 6.40 ms: 1.02x faster                                              |
| deepcopy_memo          | 35.0 us                                                                | 34.4 us: 1.02x faster                                              |
| regex_effbot           | 3.61 ms                                                                | 3.57 ms: 1.01x faster                                              |
| xml_etree_parse        | 150 ms                                                                 | 148 ms: 1.01x faster                                               |
| regex_compile          | 135 ms                                                                 | 134 ms: 1.01x faster                                               |
| richards               | 44.3 ms                                                                | 43.9 ms: 1.01x faster                                              |
| logging_silent         | 97.0 ns                                                                | 96.1 ns: 1.01x faster                                              |
| hexiom                 | 6.16 ms                                                                | 6.11 ms: 1.01x faster                                              |
| logging_format         | 6.52 us                                                                | 6.47 us: 1.01x faster                                              |
| regex_dna              | 209 ms                                                                 | 208 ms: 1.01x faster                                               |
| deepcopy               | 333 us                                                                 | 331 us: 1.01x faster                                               |
| pidigits               | 188 ms                                                                 | 188 ms: 1.00x faster                                               |
| create_gc_cycles       | 1.48 ms                                                                | 1.48 ms: 1.00x slower                                              |
| sympy_sum              | 167 ms                                                                 | 167 ms: 1.00x slower                                               |
| xml_etree_generate     | 81.7 ms                                                                | 82.1 ms: 1.00x slower                                              |
| asyncio_tcp            | 506 ms                                                                 | 509 ms: 1.01x slower                                               |
| deepcopy_reduce        | 3.03 us                                                                | 3.05 us: 1.01x slower                                              |
| sympy_str              | 285 ms                                                                 | 287 ms: 1.01x slower                                               |
| sympy_integrate        | 20.5 ms                                                                | 20.6 ms: 1.01x slower                                              |
| django_template        | 33.8 ms                                                                | 34.0 ms: 1.01x slower                                              |
| spectral_norm          | 93.0 ms                                                                | 93.6 ms: 1.01x slower                                              |
| pickle                 | 10.4 us                                                                | 10.4 us: 1.01x slower                                              |
| pickle_dict            | 30.5 us                                                                | 30.7 us: 1.01x slower                                              |
| sqlglot_transpile      | 1.74 ms                                                                | 1.75 ms: 1.01x slower                                              |
| python_startup_no_site | 6.50 ms                                                                | 6.55 ms: 1.01x slower                                              |
| logging_simple         | 5.90 us                                                                | 5.95 us: 1.01x slower                                              |
| 2to3                   | 251 ms                                                                 | 253 ms: 1.01x slower                                               |
| python_startup         | 8.79 ms                                                                | 8.87 ms: 1.01x slower                                              |
| comprehensions         | 24.0 us                                                                | 24.2 us: 1.01x slower                                              |
| pprint_pformat         | 1.42 sec                                                               | 1.43 sec: 1.01x slower                                             |
| async_tree_io          | 1.30 sec                                                               | 1.32 sec: 1.01x slower                                             |
| sqlglot_parse          | 1.45 ms                                                                | 1.46 ms: 1.01x slower                                              |
| genshi_text            | 21.8 ms                                                                | 22.0 ms: 1.01x slower                                              |
| scimark_monte_carlo    | 66.0 ms                                                                | 66.7 ms: 1.01x slower                                              |
| sqlglot_optimize       | 51.6 ms                                                                | 52.2 ms: 1.01x slower                                              |
| docutils               | 2.54 sec                                                               | 2.57 sec: 1.01x slower                                             |
| sympy_expand           | 462 ms                                                                 | 468 ms: 1.01x slower                                               |
| sqlglot_normalize      | 107 ms                                                                 | 108 ms: 1.01x slower                                               |
| mypy2                  | 333 ms                                                                 | 337 ms: 1.01x slower                                               |
| bench_thread_pool      | 788 us                                                                 | 799 us: 1.01x slower                                               |
| pprint_safe_repr       | 689 ms                                                                 | 698 ms: 1.01x slower                                               |
| tornado_http           | 91.1 ms                                                                | 92.3 ms: 1.01x slower                                              |
| xml_etree_iterparse    | 99.2 ms                                                                | 101 ms: 1.01x slower                                               |
| json_dumps             | 9.57 ms                                                                | 9.71 ms: 1.01x slower                                              |
| genshi_xml             | 48.1 ms                                                                | 48.9 ms: 1.02x slower                                              |
| pickle_pure_python     | 287 us                                                                 | 292 us: 1.02x slower                                               |
| json_loads             | 23.8 us                                                                | 24.2 us: 1.02x slower                                              |
| async_generators       | 409 ms                                                                 | 416 ms: 1.02x slower                                               |
| async_tree_none        | 525 ms                                                                 | 535 ms: 1.02x slower                                               |
| nqueens                | 79.6 ms                                                                | 81.2 ms: 1.02x slower                                              |
| xml_etree_process      | 56.8 ms                                                                | 58.0 ms: 1.02x slower                                              |
| dulwich_log            | 63.2 ms                                                                | 64.6 ms: 1.02x slower                                              |
| pycparser              | 1.15 sec                                                               | 1.18 sec: 1.02x slower                                             |
| go                     | 134 ms                                                                 | 137 ms: 1.02x slower                                               |
| meteor_contest         | 102 ms                                                                 | 104 ms: 1.02x slower                                               |
| json                   | 4.58 ms                                                                | 4.68 ms: 1.02x slower                                              |
| html5lib               | 61.1 ms                                                                | 62.4 ms: 1.02x slower                                              |
| thrift                 | 787 us                                                                 | 804 us: 1.02x slower                                               |
| pickle_list            | 4.24 us                                                                | 4.33 us: 1.02x slower                                              |
| dask                   | 503 ms                                                                 | 515 ms: 1.02x slower                                               |
| raytrace               | 285 ms                                                                 | 293 ms: 1.03x slower                                               |
| chameleon              | 6.45 ms                                                                | 6.63 ms: 1.03x slower                                              |
| deltablue              | 3.23 ms                                                                | 3.32 ms: 1.03x slower                                              |
| chaos                  | 65.3 ms                                                                | 67.3 ms: 1.03x slower                                              |
| fannkuch               | 375 ms                                                                 | 387 ms: 1.03x slower                                               |
| unpickle               | 13.3 us                                                                | 13.8 us: 1.03x slower                                              |
| async_tree_memoization | 650 ms                                                                 | 676 ms: 1.04x slower                                               |
| coroutines             | 21.9 ms                                                                | 22.7 ms: 1.04x slower                                              |
| unpack_sequence        | 42.4 ns                                                                | 44.7 ns: 1.05x slower                                              |
| unpickle_list          | 4.98 us                                                                | 5.28 us: 1.06x slower                                              |
| pyflate                | 408 ms                                                                 | 434 ms: 1.06x slower                                               |
| gc_traversal           | 3.67 ms                                                                | 4.06 ms: 1.11x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (13): scimark_lu, unpickle_pure_python, crypto_pyaes, float, mako, scimark_sor, regex_v8, pathlib, bench_mp_pool, scimark_sparse_mat_mult, generators, sqlite_synth, async_tree_cpu_io_mixed
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20230322-3.12.0a6+-87be8d9/bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9.json: aiohttp, coverage, djangocms, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
