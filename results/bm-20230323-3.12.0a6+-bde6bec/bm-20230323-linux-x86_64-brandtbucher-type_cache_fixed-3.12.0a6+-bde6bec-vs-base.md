
# Results vs. base

- fork: brandtbucher
- ref: type_cache_fixed
- machine: linux-x86_64
- commit hash: bde6bec
- commit date: 2023-03-23
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                     |
| chameleon      | 6.45 ms                                                                | 6.55 ms: 1.01x slower                                                    |
| docutils       | 2.54 sec                                                               | 2.56 sec: 1.01x slower                                                   |
| html5lib       | 61.1 ms                                                                | 62.2 ms: 1.02x slower                                                    |
| tornado_http   | 91.1 ms                                                                | 92.7 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 88.6 ms                                                                | 90.2 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 209 ms                                                                 | 204 ms: 1.03x faster                                                     |
| regex_effbot   | 3.61 ms                                                                | 3.57 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 150 ms                                                                 | 147 ms: 1.02x faster                                                     |
| xml_etree_process   | 56.8 ms                                                                | 56.5 ms: 1.01x faster                                                    |
| json_dumps          | 9.57 ms                                                                | 9.53 ms: 1.00x faster                                                    |
| xml_etree_iterparse | 99.2 ms                                                                | 100 ms: 1.01x slower                                                     |
| pickle              | 10.4 us                                                                | 10.5 us: 1.01x slower                                                    |
| json_loads          | 23.8 us                                                                | 24.1 us: 1.01x slower                                                    |
| unpickle_list       | 4.98 us                                                                | 5.07 us: 1.02x slower                                                    |
| unpickle            | 13.3 us                                                                | 13.8 us: 1.04x slower                                                    |
| pickle_dict         | 30.5 us                                                                | 31.9 us: 1.04x slower                                                    |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (4): pickle_pure_python, pickle_list, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.79 ms                                                                | 8.83 ms: 1.00x slower                                                    |
| python_startup_no_site | 6.50 ms                                                                | 6.53 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 10.1 ms                                                                | 9.96 ms: 1.01x faster                                                    |
| genshi_text    | 21.8 ms                                                                | 22.2 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                    | 2.71 sec                                                               | 2.54 sec: 1.07x faster                                                   |
| gc_traversal           | 3.67 ms                                                                | 3.54 ms: 1.04x faster                                                    |
| regex_dna              | 209 ms                                                                 | 204 ms: 1.03x faster                                                     |
| pathlib                | 18.2 ms                                                                | 17.7 ms: 1.03x faster                                                    |
| unpack_sequence        | 42.4 ns                                                                | 41.6 ns: 1.02x faster                                                    |
| logging_format         | 6.52 us                                                                | 6.40 us: 1.02x faster                                                    |
| xml_etree_parse        | 150 ms                                                                 | 147 ms: 1.02x faster                                                     |
| deepcopy_memo          | 35.0 us                                                                | 34.5 us: 1.02x faster                                                    |
| regex_effbot           | 3.61 ms                                                                | 3.57 ms: 1.01x faster                                                    |
| logging_simple         | 5.90 us                                                                | 5.83 us: 1.01x faster                                                    |
| deepcopy               | 333 us                                                                 | 330 us: 1.01x faster                                                     |
| mako                   | 10.1 ms                                                                | 9.96 ms: 1.01x faster                                                    |
| raytrace               | 285 ms                                                                 | 283 ms: 1.01x faster                                                     |
| xml_etree_process      | 56.8 ms                                                                | 56.5 ms: 1.01x faster                                                    |
| pprint_pformat         | 1.42 sec                                                               | 1.41 sec: 1.01x faster                                                   |
| json_dumps             | 9.57 ms                                                                | 9.53 ms: 1.00x faster                                                    |
| comprehensions         | 24.0 us                                                                | 23.9 us: 1.00x faster                                                    |
| 2to3                   | 251 ms                                                                 | 252 ms: 1.00x slower                                                     |
| sympy_integrate        | 20.5 ms                                                                | 20.6 ms: 1.00x slower                                                    |
| python_startup         | 8.79 ms                                                                | 8.83 ms: 1.00x slower                                                    |
| python_startup_no_site | 6.50 ms                                                                | 6.53 ms: 1.00x slower                                                    |
| asyncio_tcp            | 506 ms                                                                 | 509 ms: 1.01x slower                                                     |
| scimark_sor            | 108 ms                                                                 | 109 ms: 1.01x slower                                                     |
| docutils               | 2.54 sec                                                               | 2.56 sec: 1.01x slower                                                   |
| sqlglot_optimize       | 51.6 ms                                                                | 52.0 ms: 1.01x slower                                                    |
| xml_etree_iterparse    | 99.2 ms                                                                | 100 ms: 1.01x slower                                                     |
| bench_thread_pool      | 788 us                                                                 | 796 us: 1.01x slower                                                     |
| pickle                 | 10.4 us                                                                | 10.5 us: 1.01x slower                                                    |
| sympy_expand           | 462 ms                                                                 | 467 ms: 1.01x slower                                                     |
| fannkuch               | 375 ms                                                                 | 379 ms: 1.01x slower                                                     |
| pycparser              | 1.15 sec                                                               | 1.17 sec: 1.01x slower                                                   |
| async_tree_io          | 1.30 sec                                                               | 1.32 sec: 1.01x slower                                                   |
| sqlglot_transpile      | 1.74 ms                                                                | 1.76 ms: 1.01x slower                                                    |
| mypy2                  | 333 ms                                                                 | 337 ms: 1.01x slower                                                     |
| dulwich_log            | 63.2 ms                                                                | 64.1 ms: 1.01x slower                                                    |
| json_loads             | 23.8 us                                                                | 24.1 us: 1.01x slower                                                    |
| coverage               | 95.0 ms                                                                | 96.3 ms: 1.01x slower                                                    |
| spectral_norm          | 93.0 ms                                                                | 94.3 ms: 1.01x slower                                                    |
| sqlglot_parse          | 1.45 ms                                                                | 1.47 ms: 1.01x slower                                                    |
| logging_silent         | 97.0 ns                                                                | 98.4 ns: 1.01x slower                                                    |
| chameleon              | 6.45 ms                                                                | 6.55 ms: 1.01x slower                                                    |
| generators             | 29.3 ms                                                                | 29.7 ms: 1.02x slower                                                    |
| crypto_pyaes           | 73.9 ms                                                                | 75.1 ms: 1.02x slower                                                    |
| gunicorn               | 1.08 ms                                                                | 1.10 ms: 1.02x slower                                                    |
| tornado_http           | 91.1 ms                                                                | 92.7 ms: 1.02x slower                                                    |
| html5lib               | 61.1 ms                                                                | 62.2 ms: 1.02x slower                                                    |
| nbody                  | 88.6 ms                                                                | 90.2 ms: 1.02x slower                                                    |
| genshi_text            | 21.8 ms                                                                | 22.2 ms: 1.02x slower                                                    |
| unpickle_list          | 4.98 us                                                                | 5.07 us: 1.02x slower                                                    |
| dask                   | 503 ms                                                                 | 512 ms: 1.02x slower                                                     |
| meteor_contest         | 102 ms                                                                 | 104 ms: 1.02x slower                                                     |
| json                   | 4.58 ms                                                                | 4.67 ms: 1.02x slower                                                    |
| scimark_lu             | 108 ms                                                                 | 111 ms: 1.02x slower                                                     |
| thrift                 | 787 us                                                                 | 806 us: 1.03x slower                                                     |
| scimark_monte_carlo    | 66.0 ms                                                                | 67.6 ms: 1.03x slower                                                    |
| pyflate                | 408 ms                                                                 | 419 ms: 1.03x slower                                                     |
| nqueens                | 79.6 ms                                                                | 81.9 ms: 1.03x slower                                                    |
| go                     | 134 ms                                                                 | 138 ms: 1.03x slower                                                     |
| async_tree_memoization | 650 ms                                                                 | 673 ms: 1.03x slower                                                     |
| chaos                  | 65.3 ms                                                                | 67.7 ms: 1.04x slower                                                    |
| unpickle               | 13.3 us                                                                | 13.8 us: 1.04x slower                                                    |
| pickle_dict            | 30.5 us                                                                | 31.9 us: 1.04x slower                                                    |
| coroutines             | 21.9 ms                                                                | 23.0 ms: 1.05x slower                                                    |
| deltablue              | 3.23 ms                                                                | 3.40 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (27): regex_compile, telco, scimark_fft, richards, deepcopy_reduce, hexiom, sympy_sum, django_template, sympy_str, pickle_pure_python, bench_mp_pool, pidigits, create_gc_cycles, pprint_safe_repr, genshi_xml, pickle_list, regex_v8, sqlglot_normalize, float, xml_etree_generate, sqlite_synth, unpickle_pure_python, async_generators, scimark_sparse_mat_mult, async_tree_cpu_io_mixed, djangocms, async_tree_none
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20230322-3.12.0a6+-87be8d9/bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9.json: aiohttp, sqlalchemy_declarative, sqlalchemy_imperative
