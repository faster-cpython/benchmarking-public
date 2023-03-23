
# Results vs. base

- fork: brandtbucher
- ref: type_cache_fixed
- machine: linux-x86_64
- commit hash: 212046c
- commit date: 2023-03-23
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 251 ms: 1.00x faster                                                     |
| docutils       | 2.54 sec                                                               | 2.53 sec: 1.01x faster                                                   |
| tornado_http   | 91.1 ms                                                                | 92.5 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 73.8 ms                                                                | 73.1 ms: 1.01x faster                                                    |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                                | 3.37 ms: 1.07x faster                                                    |
| regex_v8       | 22.4 ms                                                                | 21.6 ms: 1.04x faster                                                    |
| regex_dna      | 209 ms                                                                 | 203 ms: 1.03x faster                                                     |
| regex_compile  | 135 ms                                                                 | 132 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process  | 56.8 ms                                                                | 56.0 ms: 1.02x faster                                                    |
| xml_etree_parse    | 150 ms                                                                 | 148 ms: 1.01x faster                                                     |
| xml_etree_generate | 81.7 ms                                                                | 80.9 ms: 1.01x faster                                                    |
| pickle             | 10.4 us                                                                | 10.4 us: 1.00x slower                                                    |
| pickle_list        | 4.24 us                                                                | 4.27 us: 1.01x slower                                                    |
| pickle_dict        | 30.5 us                                                                | 30.8 us: 1.01x slower                                                    |
| json_loads         | 23.8 us                                                                | 24.2 us: 1.02x slower                                                    |
| unpickle_list      | 4.98 us                                                                | 5.25 us: 1.05x slower                                                    |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (5): json_dumps, unpickle_pure_python, pickle_pure_python, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.79 ms                                                                | 8.82 ms: 1.00x slower                                                    |
| python_startup_no_site | 6.50 ms                                                                | 6.53 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 33.8 ms                                                                | 33.0 ms: 1.03x faster                                                    |
| genshi_text     | 21.8 ms                                                                | 21.6 ms: 1.01x faster                                                    |
| mako            | 10.1 ms                                                                | 10.1 ms: 1.00x slower                                                    |
| genshi_xml      | 48.1 ms                                                                | 48.4 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                     | 2.71 sec                                                               | 2.51 sec: 1.08x faster                                                   |
| regex_effbot            | 3.61 ms                                                                | 3.37 ms: 1.07x faster                                                    |
| pycparser               | 1.15 sec                                                               | 1.10 sec: 1.05x faster                                                   |
| gc_traversal            | 3.67 ms                                                                | 3.53 ms: 1.04x faster                                                    |
| regex_v8                | 22.4 ms                                                                | 21.6 ms: 1.04x faster                                                    |
| regex_dna               | 209 ms                                                                 | 203 ms: 1.03x faster                                                     |
| django_template         | 33.8 ms                                                                | 33.0 ms: 1.03x faster                                                    |
| spectral_norm           | 93.0 ms                                                                | 90.9 ms: 1.02x faster                                                    |
| scimark_fft             | 319 ms                                                                 | 312 ms: 1.02x faster                                                     |
| regex_compile           | 135 ms                                                                 | 132 ms: 1.02x faster                                                     |
| unpack_sequence         | 42.4 ns                                                                | 41.7 ns: 1.02x faster                                                    |
| xml_etree_process       | 56.8 ms                                                                | 56.0 ms: 1.02x faster                                                    |
| pathlib                 | 18.2 ms                                                                | 17.9 ms: 1.01x faster                                                    |
| xml_etree_parse         | 150 ms                                                                 | 148 ms: 1.01x faster                                                     |
| fannkuch                | 375 ms                                                                 | 370 ms: 1.01x faster                                                     |
| hexiom                  | 6.16 ms                                                                | 6.08 ms: 1.01x faster                                                    |
| deepcopy_reduce         | 3.03 us                                                                | 3.00 us: 1.01x faster                                                    |
| telco                   | 6.52 ms                                                                | 6.45 ms: 1.01x faster                                                    |
| float                   | 73.8 ms                                                                | 73.1 ms: 1.01x faster                                                    |
| pprint_pformat          | 1.42 sec                                                               | 1.40 sec: 1.01x faster                                                   |
| xml_etree_generate      | 81.7 ms                                                                | 80.9 ms: 1.01x faster                                                    |
| deepcopy_memo           | 35.0 us                                                                | 34.7 us: 1.01x faster                                                    |
| logging_format          | 6.52 us                                                                | 6.46 us: 1.01x faster                                                    |
| go                      | 134 ms                                                                 | 133 ms: 1.01x faster                                                     |
| genshi_text             | 21.8 ms                                                                | 21.6 ms: 1.01x faster                                                    |
| deepcopy                | 333 us                                                                 | 330 us: 1.01x faster                                                     |
| sqlite_synth            | 2.61 us                                                                | 2.59 us: 1.01x faster                                                    |
| sympy_str               | 285 ms                                                                 | 284 ms: 1.01x faster                                                     |
| docutils                | 2.54 sec                                                               | 2.53 sec: 1.01x faster                                                   |
| sympy_expand            | 462 ms                                                                 | 460 ms: 1.00x faster                                                     |
| pprint_safe_repr        | 689 ms                                                                 | 686 ms: 1.00x faster                                                     |
| sympy_sum               | 167 ms                                                                 | 166 ms: 1.00x faster                                                     |
| sqlglot_normalize       | 107 ms                                                                 | 107 ms: 1.00x faster                                                     |
| 2to3                    | 251 ms                                                                 | 251 ms: 1.00x faster                                                     |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                     |
| python_startup          | 8.79 ms                                                                | 8.82 ms: 1.00x slower                                                    |
| python_startup_no_site  | 6.50 ms                                                                | 6.53 ms: 1.00x slower                                                    |
| mako                    | 10.1 ms                                                                | 10.1 ms: 1.00x slower                                                    |
| sqlglot_optimize        | 51.6 ms                                                                | 51.8 ms: 1.00x slower                                                    |
| pickle                  | 10.4 us                                                                | 10.4 us: 1.00x slower                                                    |
| gunicorn                | 1.08 ms                                                                | 1.09 ms: 1.00x slower                                                    |
| asyncio_tcp             | 506 ms                                                                 | 510 ms: 1.01x slower                                                     |
| genshi_xml              | 48.1 ms                                                                | 48.4 ms: 1.01x slower                                                    |
| mypy2                   | 333 ms                                                                 | 335 ms: 1.01x slower                                                     |
| thrift                  | 787 us                                                                 | 792 us: 1.01x slower                                                     |
| scimark_sor             | 108 ms                                                                 | 109 ms: 1.01x slower                                                     |
| bench_thread_pool       | 788 us                                                                 | 794 us: 1.01x slower                                                     |
| pickle_list             | 4.24 us                                                                | 4.27 us: 1.01x slower                                                    |
| dulwich_log             | 63.2 ms                                                                | 63.8 ms: 1.01x slower                                                    |
| pickle_dict             | 30.5 us                                                                | 30.8 us: 1.01x slower                                                    |
| raytrace                | 285 ms                                                                 | 288 ms: 1.01x slower                                                     |
| deltablue               | 3.23 ms                                                                | 3.27 ms: 1.01x slower                                                    |
| tornado_http            | 91.1 ms                                                                | 92.5 ms: 1.02x slower                                                    |
| scimark_monte_carlo     | 66.0 ms                                                                | 67.0 ms: 1.02x slower                                                    |
| async_generators        | 409 ms                                                                 | 416 ms: 1.02x slower                                                     |
| json_loads              | 23.8 us                                                                | 24.2 us: 1.02x slower                                                    |
| generators              | 29.3 ms                                                                | 29.8 ms: 1.02x slower                                                    |
| dask                    | 503 ms                                                                 | 512 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult | 4.21 ms                                                                | 4.29 ms: 1.02x slower                                                    |
| chaos                   | 65.3 ms                                                                | 66.6 ms: 1.02x slower                                                    |
| coverage                | 95.0 ms                                                                | 97.0 ms: 1.02x slower                                                    |
| meteor_contest          | 102 ms                                                                 | 104 ms: 1.02x slower                                                     |
| pyflate                 | 408 ms                                                                 | 418 ms: 1.03x slower                                                     |
| json                    | 4.58 ms                                                                | 4.70 ms: 1.03x slower                                                    |
| scimark_lu              | 108 ms                                                                 | 111 ms: 1.03x slower                                                     |
| coroutines              | 21.9 ms                                                                | 22.6 ms: 1.03x slower                                                    |
| async_tree_memoization  | 650 ms                                                                 | 673 ms: 1.03x slower                                                     |
| unpickle_list           | 4.98 us                                                                | 5.25 us: 1.05x slower                                                    |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (24): nbody, richards, nqueens, comprehensions, create_gc_cycles, json_dumps, unpickle_pure_python, pickle_pure_python, sqlglot_transpile, async_tree_none, crypto_pyaes, bench_mp_pool, xml_etree_iterparse, sympy_integrate, aiohttp, sqlglot_parse, logging_simple, logging_silent, chameleon, async_tree_io, djangocms, html5lib, async_tree_cpu_io_mixed, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20230322-3.12.0a6+-87be8d9/bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9.json: sqlalchemy_declarative, sqlalchemy_imperative
