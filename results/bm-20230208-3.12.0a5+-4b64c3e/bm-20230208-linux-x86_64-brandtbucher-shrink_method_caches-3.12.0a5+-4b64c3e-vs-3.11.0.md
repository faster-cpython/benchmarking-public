
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 4b64c3e
- commit date: 2023-02-08
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                         |
| chameleon      | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                        |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                       |
| html5lib       | 63.2 ms                                                | 61.0 ms: 1.03x faster                                                        |
| tornado_http   | 96.6 ms                                                | 94.8 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 73.0 ms: 1.05x faster                                                        |
| pidigits       | 199 ms                                                 | 192 ms: 1.04x faster                                                         |
| nbody          | 95.0 ms                                                | 93.1 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                         |
| regex_v8       | 22.3 ms                                                | 22.0 ms: 1.01x faster                                                        |
| regex_effbot   | 3.36 ms                                                | 3.52 ms: 1.05x slower                                                        |
| regex_dna      | 203 ms                                                 | 218 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.33 ms: 1.36x faster                                                        |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                                         |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| pickle_dict          | 31.4 us                                                | 30.4 us: 1.03x faster                                                        |
| pickle_pure_python   | 304 us                                                 | 294 us: 1.03x faster                                                         |
| pickle_list          | 4.17 us                                                | 4.13 us: 1.01x faster                                                        |
| unpickle_list        | 4.95 us                                                | 4.98 us: 1.01x slower                                                        |
| xml_etree_process    | 53.8 ms                                                | 55.3 ms: 1.03x slower                                                        |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 80.5 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.86 ms: 1.06x slower                                                        |
| python_startup_no_site | 5.96 ms                                                | 6.42 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 47.0 ms: 1.11x faster                                                        |
| genshi_text    | 22.1 ms                                                | 20.8 ms: 1.06x faster                                                        |
| mako           | 9.85 ms                                                | 9.90 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.33 ms: 1.36x faster                                                        |
| deltablue               | 3.64 ms                                                | 3.19 ms: 1.14x faster                                                        |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                                         |
| nqueens                 | 85.0 ms                                                | 76.2 ms: 1.12x faster                                                        |
| genshi_xml              | 52.1 ms                                                | 47.0 ms: 1.11x faster                                                        |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                                        |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                         |
| richards                | 46.2 ms                                                | 42.8 ms: 1.08x faster                                                        |
| fannkuch                | 388 ms                                                 | 361 ms: 1.08x faster                                                         |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                         |
| pycparser               | 1.17 sec                                               | 1.09 sec: 1.07x faster                                                       |
| spectral_norm           | 99.9 ms                                                | 93.4 ms: 1.07x faster                                                        |
| scimark_fft             | 329 ms                                                 | 308 ms: 1.07x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| coroutines              | 26.1 ms                                                | 24.5 ms: 1.06x faster                                                        |
| hexiom                  | 6.35 ms                                                | 5.96 ms: 1.06x faster                                                        |
| genshi_text             | 22.1 ms                                                | 20.8 ms: 1.06x faster                                                        |
| json                    | 4.95 ms                                                | 4.66 ms: 1.06x faster                                                        |
| sympy_str               | 287 ms                                                 | 271 ms: 1.06x faster                                                         |
| deepcopy_memo           | 36.4 us                                                | 34.5 us: 1.06x faster                                                        |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                         |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                                        |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                                         |
| float                   | 76.3 ms                                                | 73.0 ms: 1.05x faster                                                        |
| sympy_expand            | 472 ms                                                 | 452 ms: 1.05x faster                                                         |
| deepcopy                | 344 us                                                 | 331 us: 1.04x faster                                                         |
| pidigits                | 199 ms                                                 | 192 ms: 1.04x faster                                                         |
| html5lib                | 63.2 ms                                                | 61.0 ms: 1.03x faster                                                        |
| pickle_dict             | 31.4 us                                                | 30.4 us: 1.03x faster                                                        |
| chaos                   | 68.6 ms                                                | 66.4 ms: 1.03x faster                                                        |
| telco                   | 6.62 ms                                                | 6.41 ms: 1.03x faster                                                        |
| pickle_pure_python      | 304 us                                                 | 294 us: 1.03x faster                                                         |
| scimark_monte_carlo     | 68.3 ms                                                | 66.1 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.27 ms: 1.03x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 1.02 ms: 1.03x faster                                                        |
| pyflate                 | 417 ms                                                 | 406 ms: 1.03x faster                                                         |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                        |
| logging_silent          | 98.5 ns                                                | 95.9 ns: 1.03x faster                                                        |
| bench_thread_pool       | 810 us                                                 | 791 us: 1.02x faster                                                         |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                       |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                         |
| sqlglot_optimize        | 53.0 ms                                                | 51.8 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                | 2.90 us: 1.02x faster                                                        |
| nbody                   | 95.0 ms                                                | 93.1 ms: 1.02x faster                                                        |
| logging_format          | 6.62 us                                                | 6.49 us: 1.02x faster                                                        |
| tornado_http            | 96.6 ms                                                | 94.8 ms: 1.02x faster                                                        |
| logging_simple          | 6.06 us                                                | 5.95 us: 1.02x faster                                                        |
| meteor_contest          | 105 ms                                                 | 103 ms: 1.02x faster                                                         |
| pprint_pformat          | 1.44 sec                                               | 1.42 sec: 1.02x faster                                                       |
| raytrace                | 290 ms                                                 | 286 ms: 1.02x faster                                                         |
| regex_v8                | 22.3 ms                                                | 22.0 ms: 1.01x faster                                                        |
| async_tree_none         | 529 ms                                                 | 524 ms: 1.01x faster                                                         |
| sqlalchemy_declarative  | 139 ms                                                 | 137 ms: 1.01x faster                                                         |
| pickle_list             | 4.17 us                                                | 4.13 us: 1.01x faster                                                        |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                        |
| chameleon               | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 691 ms                                                 | 686 ms: 1.01x faster                                                         |
| dulwich_log             | 63.9 ms                                                | 63.6 ms: 1.01x faster                                                        |
| crypto_pyaes            | 73.9 ms                                                | 73.6 ms: 1.00x faster                                                        |
| mako                    | 9.85 ms                                                | 9.90 ms: 1.01x slower                                                        |
| unpickle_list           | 4.95 us                                                | 4.98 us: 1.01x slower                                                        |
| thrift                  | 752 us                                                 | 759 us: 1.01x slower                                                         |
| unpack_sequence         | 43.4 ns                                                | 44.2 ns: 1.02x slower                                                        |
| sqlalchemy_imperative   | 18.0 ms                                                | 18.4 ms: 1.02x slower                                                        |
| xml_etree_process       | 53.8 ms                                                | 55.3 ms: 1.03x slower                                                        |
| mdp                     | 2.62 sec                                               | 2.70 sec: 1.03x slower                                                       |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                        |
| async_tree_memoization  | 625 ms                                                 | 645 ms: 1.03x slower                                                         |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.52 ms: 1.05x slower                                                        |
| sqlglot_transpile       | 1.66 ms                                                | 1.74 ms: 1.05x slower                                                        |
| sqlglot_parse           | 1.37 ms                                                | 1.45 ms: 1.05x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 80.5 ms: 1.06x slower                                                        |
| python_startup          | 8.36 ms                                                | 8.86 ms: 1.06x slower                                                        |
| generators              | 72.2 ms                                                | 76.9 ms: 1.07x slower                                                        |
| regex_dna               | 203 ms                                                 | 218 ms: 1.07x slower                                                         |
| python_startup_no_site  | 5.96 ms                                                | 6.42 ms: 1.08x slower                                                        |
| async_generators        | 359 ms                                                 | 435 ms: 1.21x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, sqlglot_normalize, bench_mp_pool, django_template, coverage, xml_etree_iterparse, scimark_lu, async_tree_io, unpickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230208-3.12.0a5+-4b64c3e/bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
