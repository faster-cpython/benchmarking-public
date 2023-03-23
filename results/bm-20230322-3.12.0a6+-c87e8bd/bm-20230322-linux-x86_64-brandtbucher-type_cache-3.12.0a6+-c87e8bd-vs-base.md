
# Results vs. base

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: c87e8bd
- commit date: 2023-03-22
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 253 ms: 1.01x slower                                               |
| chameleon      | 6.45 ms                                                                | 6.64 ms: 1.03x slower                                              |
| docutils       | 2.54 sec                                                               | 2.56 sec: 1.01x slower                                             |
| tornado_http   | 91.1 ms                                                                | 91.7 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x faster                                               |
| float          | 73.8 ms                                                                | 74.4 ms: 1.01x slower                                              |
| nbody          | 88.6 ms                                                                | 90.6 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                                | 3.57 ms: 1.01x faster                                              |
| regex_dna      | 209 ms                                                                 | 208 ms: 1.01x faster                                               |
| regex_v8       | 22.4 ms                                                                | 22.8 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle               | 10.4 us                                                                | 10.2 us: 1.01x faster                                              |
| pickle_list          | 4.24 us                                                                | 4.21 us: 1.01x faster                                              |
| xml_etree_process    | 56.8 ms                                                                | 57.3 ms: 1.01x slower                                              |
| pickle_pure_python   | 287 us                                                                 | 290 us: 1.01x slower                                               |
| xml_etree_parse      | 150 ms                                                                 | 152 ms: 1.01x slower                                               |
| unpickle_pure_python | 201 us                                                                 | 203 us: 1.01x slower                                               |
| json_dumps           | 9.57 ms                                                                | 9.70 ms: 1.01x slower                                              |
| pickle_dict          | 30.5 us                                                                | 31.1 us: 1.02x slower                                              |
| json_loads           | 23.8 us                                                                | 24.2 us: 1.02x slower                                              |
| xml_etree_iterparse  | 99.2 ms                                                                | 103 ms: 1.03x slower                                               |
| unpickle_list        | 4.98 us                                                                | 5.20 us: 1.04x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.56 ms: 1.01x slower                                              |
| python_startup         | 8.79 ms                                                                | 8.88 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 33.8 ms                                                                | 33.2 ms: 1.02x faster                                              |
| mako            | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                              |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark              | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                    | 2.71 sec                                                               | 2.51 sec: 1.08x faster                                             |
| scimark_fft            | 319 ms                                                                 | 307 ms: 1.04x faster                                               |
| deepcopy_reduce        | 3.03 us                                                                | 2.94 us: 1.03x faster                                              |
| spectral_norm          | 93.0 ms                                                                | 90.4 ms: 1.03x faster                                              |
| hexiom                 | 6.16 ms                                                                | 6.04 ms: 1.02x faster                                              |
| django_template        | 33.8 ms                                                                | 33.2 ms: 1.02x faster                                              |
| pathlib                | 18.2 ms                                                                | 17.9 ms: 1.02x faster                                              |
| pickle                 | 10.4 us                                                                | 10.2 us: 1.01x faster                                              |
| scimark_sor            | 108 ms                                                                 | 107 ms: 1.01x faster                                               |
| regex_effbot           | 3.61 ms                                                                | 3.57 ms: 1.01x faster                                              |
| logging_format         | 6.52 us                                                                | 6.47 us: 1.01x faster                                              |
| richards               | 44.3 ms                                                                | 44.0 ms: 1.01x faster                                              |
| pickle_list            | 4.24 us                                                                | 4.21 us: 1.01x faster                                              |
| regex_dna              | 209 ms                                                                 | 208 ms: 1.01x faster                                               |
| mako                   | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                              |
| sympy_str              | 285 ms                                                                 | 284 ms: 1.00x faster                                               |
| pidigits               | 188 ms                                                                 | 188 ms: 1.00x faster                                               |
| dulwich_log            | 63.2 ms                                                                | 63.4 ms: 1.00x slower                                              |
| sqlglot_normalize      | 107 ms                                                                 | 108 ms: 1.00x slower                                               |
| asyncio_tcp            | 506 ms                                                                 | 509 ms: 1.01x slower                                               |
| pprint_safe_repr       | 689 ms                                                                 | 693 ms: 1.01x slower                                               |
| pprint_pformat         | 1.42 sec                                                               | 1.42 sec: 1.01x slower                                             |
| sympy_expand           | 462 ms                                                                 | 465 ms: 1.01x slower                                               |
| tornado_http           | 91.1 ms                                                                | 91.7 ms: 1.01x slower                                              |
| create_gc_cycles       | 1.48 ms                                                                | 1.49 ms: 1.01x slower                                              |
| 2to3                   | 251 ms                                                                 | 253 ms: 1.01x slower                                               |
| sqlglot_parse          | 1.45 ms                                                                | 1.46 ms: 1.01x slower                                              |
| xml_etree_process      | 56.8 ms                                                                | 57.3 ms: 1.01x slower                                              |
| bench_thread_pool      | 788 us                                                                 | 794 us: 1.01x slower                                               |
| float                  | 73.8 ms                                                                | 74.4 ms: 1.01x slower                                              |
| pycparser              | 1.15 sec                                                               | 1.16 sec: 1.01x slower                                             |
| docutils               | 2.54 sec                                                               | 2.56 sec: 1.01x slower                                             |
| mypy2                  | 333 ms                                                                 | 336 ms: 1.01x slower                                               |
| python_startup_no_site | 6.50 ms                                                                | 6.56 ms: 1.01x slower                                              |
| pickle_pure_python     | 287 us                                                                 | 290 us: 1.01x slower                                               |
| python_startup         | 8.79 ms                                                                | 8.88 ms: 1.01x slower                                              |
| nqueens                | 79.6 ms                                                                | 80.5 ms: 1.01x slower                                              |
| sqlglot_optimize       | 51.6 ms                                                                | 52.2 ms: 1.01x slower                                              |
| xml_etree_parse        | 150 ms                                                                 | 152 ms: 1.01x slower                                               |
| unpickle_pure_python   | 201 us                                                                 | 203 us: 1.01x slower                                               |
| dask                   | 503 ms                                                                 | 509 ms: 1.01x slower                                               |
| json_dumps             | 9.57 ms                                                                | 9.70 ms: 1.01x slower                                              |
| comprehensions         | 24.0 us                                                                | 24.4 us: 1.01x slower                                              |
| regex_v8               | 22.4 ms                                                                | 22.8 ms: 1.01x slower                                              |
| pickle_dict            | 30.5 us                                                                | 31.1 us: 1.02x slower                                              |
| async_generators       | 409 ms                                                                 | 417 ms: 1.02x slower                                               |
| json_loads             | 23.8 us                                                                | 24.2 us: 1.02x slower                                              |
| crypto_pyaes           | 73.9 ms                                                                | 75.3 ms: 1.02x slower                                              |
| nbody                  | 88.6 ms                                                                | 90.6 ms: 1.02x slower                                              |
| pyflate                | 408 ms                                                                 | 417 ms: 1.02x slower                                               |
| chaos                  | 65.3 ms                                                                | 67.0 ms: 1.03x slower                                              |
| async_tree_memoization | 650 ms                                                                 | 667 ms: 1.03x slower                                               |
| raytrace               | 285 ms                                                                 | 293 ms: 1.03x slower                                               |
| json                   | 4.58 ms                                                                | 4.70 ms: 1.03x slower                                              |
| scimark_monte_carlo    | 66.0 ms                                                                | 67.8 ms: 1.03x slower                                              |
| chameleon              | 6.45 ms                                                                | 6.64 ms: 1.03x slower                                              |
| coroutines             | 21.9 ms                                                                | 22.5 ms: 1.03x slower                                              |
| deltablue              | 3.23 ms                                                                | 3.33 ms: 1.03x slower                                              |
| xml_etree_iterparse    | 99.2 ms                                                                | 103 ms: 1.03x slower                                               |
| meteor_contest         | 102 ms                                                                 | 106 ms: 1.03x slower                                               |
| unpack_sequence        | 42.4 ns                                                                | 44.0 ns: 1.04x slower                                              |
| thrift                 | 787 us                                                                 | 816 us: 1.04x slower                                               |
| unpickle_list          | 4.98 us                                                                | 5.20 us: 1.04x slower                                              |
| gc_traversal           | 3.67 ms                                                                | 3.98 ms: 1.08x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (24): regex_compile, sympy_sum, deepcopy_memo, fannkuch, bench_mp_pool, logging_simple, xml_etree_generate, genshi_xml, logging_silent, deepcopy, sympy_integrate, scimark_lu, scimark_sparse_mat_mult, async_tree_io, telco, genshi_text, go, sqlite_synth, generators, sqlglot_transpile, async_tree_cpu_io_mixed, async_tree_none, unpickle, html5lib
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20230322-3.12.0a6+-87be8d9/bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9.json: aiohttp, coverage, djangocms, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
