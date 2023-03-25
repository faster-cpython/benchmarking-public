
# Results vs. base

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: 30483bd
- commit date: 2023-03-24
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 253 ms: 1.01x slower                                               |
| chameleon      | 6.45 ms                                                                | 6.54 ms: 1.01x slower                                              |
| docutils       | 2.54 sec                                                               | 2.55 sec: 1.00x slower                                             |
| tornado_http   | 91.1 ms                                                                | 92.2 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 88.6 ms                                                                | 87.6 ms: 1.01x faster                                              |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                                | 3.53 ms: 1.02x faster                                              |
| regex_dna      | 209 ms                                                                 | 208 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_list          | 4.24 us                                                                | 4.10 us: 1.03x faster                                              |
| xml_etree_process    | 56.8 ms                                                                | 56.4 ms: 1.01x faster                                              |
| xml_etree_generate   | 81.7 ms                                                                | 81.4 ms: 1.00x faster                                              |
| pickle               | 10.4 us                                                                | 10.3 us: 1.00x faster                                              |
| json_loads           | 23.8 us                                                                | 24.0 us: 1.01x slower                                              |
| pickle_pure_python   | 287 us                                                                 | 290 us: 1.01x slower                                               |
| xml_etree_parse      | 150 ms                                                                 | 151 ms: 1.01x slower                                               |
| unpickle_pure_python | 201 us                                                                 | 204 us: 1.01x slower                                               |
| unpickle_list        | 4.98 us                                                                | 5.12 us: 1.03x slower                                              |
| json_dumps           | 9.57 ms                                                                | 9.86 ms: 1.03x slower                                              |
| xml_etree_iterparse  | 99.2 ms                                                                | 104 ms: 1.05x slower                                               |
| pickle_dict          | 30.5 us                                                                | 32.3 us: 1.06x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.53 ms: 1.00x slower                                              |
| python_startup         | 8.79 ms                                                                | 8.85 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 10.1 ms                                                                | 9.95 ms: 1.01x faster                                              |
| django_template | 33.8 ms                                                                | 33.5 ms: 1.01x faster                                              |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| scimark_fft             | 319 ms                                                                 | 300 ms: 1.06x faster                                               |
| scimark_sparse_mat_mult | 4.21 ms                                                                | 4.03 ms: 1.05x faster                                              |
| pickle_list             | 4.24 us                                                                | 4.10 us: 1.03x faster                                              |
| deepcopy_reduce         | 3.03 us                                                                | 2.94 us: 1.03x faster                                              |
| richards                | 44.3 ms                                                                | 43.0 ms: 1.03x faster                                              |
| regex_effbot            | 3.61 ms                                                                | 3.53 ms: 1.02x faster                                              |
| deepcopy_memo           | 35.0 us                                                                | 34.2 us: 1.02x faster                                              |
| scimark_lu              | 108 ms                                                                 | 106 ms: 1.02x faster                                               |
| spectral_norm           | 93.0 ms                                                                | 91.5 ms: 1.02x faster                                              |
| pathlib                 | 18.2 ms                                                                | 18.0 ms: 1.01x faster                                              |
| mako                    | 10.1 ms                                                                | 9.95 ms: 1.01x faster                                              |
| nbody                   | 88.6 ms                                                                | 87.6 ms: 1.01x faster                                              |
| django_template         | 33.8 ms                                                                | 33.5 ms: 1.01x faster                                              |
| hexiom                  | 6.16 ms                                                                | 6.10 ms: 1.01x faster                                              |
| telco                   | 6.52 ms                                                                | 6.46 ms: 1.01x faster                                              |
| create_gc_cycles        | 1.48 ms                                                                | 1.46 ms: 1.01x faster                                              |
| xml_etree_process       | 56.8 ms                                                                | 56.4 ms: 1.01x faster                                              |
| regex_dna               | 209 ms                                                                 | 208 ms: 1.01x faster                                               |
| deepcopy                | 333 us                                                                 | 330 us: 1.01x faster                                               |
| sqlglot_normalize       | 107 ms                                                                 | 106 ms: 1.01x faster                                               |
| sympy_integrate         | 20.5 ms                                                                | 20.4 ms: 1.00x faster                                              |
| xml_etree_generate      | 81.7 ms                                                                | 81.4 ms: 1.00x faster                                              |
| pickle                  | 10.4 us                                                                | 10.3 us: 1.00x faster                                              |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                               |
| mdp                     | 2.71 sec                                                               | 2.71 sec: 1.00x slower                                             |
| python_startup_no_site  | 6.50 ms                                                                | 6.53 ms: 1.00x slower                                              |
| docutils                | 2.54 sec                                                               | 2.55 sec: 1.00x slower                                             |
| 2to3                    | 251 ms                                                                 | 253 ms: 1.01x slower                                               |
| sympy_expand            | 462 ms                                                                 | 465 ms: 1.01x slower                                               |
| python_startup          | 8.79 ms                                                                | 8.85 ms: 1.01x slower                                              |
| pycparser               | 1.15 sec                                                               | 1.16 sec: 1.01x slower                                             |
| logging_simple          | 5.90 us                                                                | 5.94 us: 1.01x slower                                              |
| pprint_pformat          | 1.42 sec                                                               | 1.43 sec: 1.01x slower                                             |
| asyncio_tcp             | 506 ms                                                                 | 510 ms: 1.01x slower                                               |
| comprehensions          | 24.0 us                                                                | 24.3 us: 1.01x slower                                              |
| mypy2                   | 333 ms                                                                 | 336 ms: 1.01x slower                                               |
| json_loads              | 23.8 us                                                                | 24.0 us: 1.01x slower                                              |
| pickle_pure_python      | 287 us                                                                 | 290 us: 1.01x slower                                               |
| xml_etree_parse         | 150 ms                                                                 | 151 ms: 1.01x slower                                               |
| tornado_http            | 91.1 ms                                                                | 92.2 ms: 1.01x slower                                              |
| bench_thread_pool       | 788 us                                                                 | 798 us: 1.01x slower                                               |
| async_tree_none         | 525 ms                                                                 | 531 ms: 1.01x slower                                               |
| chameleon               | 6.45 ms                                                                | 6.54 ms: 1.01x slower                                              |
| dulwich_log             | 63.2 ms                                                                | 64.1 ms: 1.01x slower                                              |
| unpickle_pure_python    | 201 us                                                                 | 204 us: 1.01x slower                                               |
| fannkuch                | 375 ms                                                                 | 381 ms: 1.02x slower                                               |
| async_generators        | 409 ms                                                                 | 416 ms: 1.02x slower                                               |
| nqueens                 | 79.6 ms                                                                | 80.9 ms: 1.02x slower                                              |
| json                    | 4.58 ms                                                                | 4.65 ms: 1.02x slower                                              |
| raytrace                | 285 ms                                                                 | 290 ms: 1.02x slower                                               |
| scimark_monte_carlo     | 66.0 ms                                                                | 67.4 ms: 1.02x slower                                              |
| thrift                  | 787 us                                                                 | 805 us: 1.02x slower                                               |
| meteor_contest          | 102 ms                                                                 | 104 ms: 1.02x slower                                               |
| pyflate                 | 408 ms                                                                 | 418 ms: 1.02x slower                                               |
| dask                    | 503 ms                                                                 | 516 ms: 1.03x slower                                               |
| deltablue               | 3.23 ms                                                                | 3.31 ms: 1.03x slower                                              |
| chaos                   | 65.3 ms                                                                | 67.0 ms: 1.03x slower                                              |
| unpickle_list           | 4.98 us                                                                | 5.12 us: 1.03x slower                                              |
| async_tree_memoization  | 650 ms                                                                 | 670 ms: 1.03x slower                                               |
| json_dumps              | 9.57 ms                                                                | 9.86 ms: 1.03x slower                                              |
| go                      | 134 ms                                                                 | 139 ms: 1.03x slower                                               |
| gc_traversal            | 3.67 ms                                                                | 3.83 ms: 1.04x slower                                              |
| coroutines              | 21.9 ms                                                                | 22.9 ms: 1.05x slower                                              |
| xml_etree_iterparse     | 99.2 ms                                                                | 104 ms: 1.05x slower                                               |
| pickle_dict             | 30.5 us                                                                | 32.3 us: 1.06x slower                                              |
| unpack_sequence         | 42.4 ns                                                                | 45.2 ns: 1.06x slower                                              |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (22): logging_silent, sqlite_synth, scimark_sor, float, unpickle, sympy_str, sympy_sum, bench_mp_pool, regex_compile, genshi_text, sqlglot_parse, genshi_xml, regex_v8, sqlglot_optimize, sqlglot_transpile, async_tree_io, logging_format, crypto_pyaes, async_tree_cpu_io_mixed, pprint_safe_repr, generators, html5lib
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20230322-3.12.0a6+-87be8d9/bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9.json: aiohttp, coverage, djangocms, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
