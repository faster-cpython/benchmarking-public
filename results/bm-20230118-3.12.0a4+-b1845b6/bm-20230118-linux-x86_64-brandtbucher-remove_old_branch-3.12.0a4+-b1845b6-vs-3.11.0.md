
# Results vs. 3.11.0

- fork: brandtbucher
- ref: remove_old_branch
- machine: linux-x86_64
- commit hash: b1845b6
- commit date: 2023-01-18
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                      |
| chameleon      | 6.38 ms                                                | 6.42 ms: 1.01x slower                                                     |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                    |
| html5lib       | 64.8 ms                                                | 59.6 ms: 1.09x faster                                                     |
| tornado_http   | 96.5 ms                                                | 93.4 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                     |
| pidigits       | 197 ms                                                 | 192 ms: 1.02x faster                                                      |
| nbody          | 90.0 ms                                                | 92.8 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                      |
| regex_v8       | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                     |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                      |
| regex_effbot   | 3.46 ms                                                | 3.64 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.42 ms: 1.31x faster                                                     |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                      |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                     |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                                      |
| xml_etree_parse      | 160 ms                                                 | 151 ms: 1.06x faster                                                      |
| xml_etree_process    | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                      |
| pickle_dict          | 31.2 us                                                | 31.9 us: 1.02x slower                                                     |
| xml_etree_generate   | 75.9 ms                                                | 77.9 ms: 1.03x slower                                                     |
| pickle_list          | 4.14 us                                                | 4.27 us: 1.03x slower                                                     |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.96 ms: 1.04x slower                                                     |
| python_startup_no_site | 6.04 ms                                                | 6.48 ms: 1.07x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                     |
| genshi_text    | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                     |
| mako           | 9.83 ms                                                | 9.70 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 489 ms: 1.81x faster                                                      |
| json_dumps              | 12.4 ms                                                | 9.42 ms: 1.31x faster                                                     |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                      |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.04 ms: 1.14x faster                                                     |
| deltablue               | 3.66 ms                                                | 3.22 ms: 1.13x faster                                                     |
| richards                | 46.1 ms                                                | 42.1 ms: 1.10x faster                                                     |
| genshi_xml              | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                     |
| nqueens                 | 83.8 ms                                                | 76.7 ms: 1.09x faster                                                     |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                     |
| html5lib                | 64.8 ms                                                | 59.6 ms: 1.09x faster                                                     |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                      |
| sympy_str               | 291 ms                                                 | 268 ms: 1.09x faster                                                      |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                                      |
| scimark_fft             | 325 ms                                                 | 303 ms: 1.07x faster                                                      |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                      |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                      |
| logging_silent          | 98.0 ns                                                | 91.6 ns: 1.07x faster                                                     |
| chaos                   | 68.7 ms                                                | 64.3 ms: 1.07x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 19.6 ms: 1.07x faster                                                     |
| unpack_sequence         | 44.5 ns                                                | 41.7 ns: 1.07x faster                                                     |
| fannkuch                | 384 ms                                                 | 362 ms: 1.06x faster                                                      |
| json                    | 4.87 ms                                                | 4.59 ms: 1.06x faster                                                     |
| float                   | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                     |
| go                      | 140 ms                                                 | 133 ms: 1.06x faster                                                      |
| xml_etree_parse         | 160 ms                                                 | 151 ms: 1.06x faster                                                      |
| deepcopy_memo           | 35.8 us                                                | 33.9 us: 1.06x faster                                                     |
| bench_thread_pool       | 817 us                                                 | 774 us: 1.05x faster                                                      |
| pyflate                 | 419 ms                                                 | 397 ms: 1.05x faster                                                      |
| coroutines              | 26.2 ms                                                | 24.8 ms: 1.05x faster                                                     |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.05x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 996 us: 1.05x faster                                                      |
| hexiom                  | 6.34 ms                                                | 6.02 ms: 1.05x faster                                                     |
| deepcopy                | 341 us                                                 | 326 us: 1.05x faster                                                      |
| logging_simple          | 6.02 us                                                | 5.76 us: 1.05x faster                                                     |
| pprint_safe_repr        | 706 ms                                                 | 676 ms: 1.04x faster                                                      |
| scimark_monte_carlo     | 68.0 ms                                                | 65.1 ms: 1.04x faster                                                     |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                     |
| crypto_pyaes            | 75.7 ms                                                | 72.6 ms: 1.04x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                    |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                                     |
| deepcopy_reduce         | 3.02 us                                                | 2.91 us: 1.04x faster                                                     |
| pycparser               | 1.19 sec                                               | 1.14 sec: 1.04x faster                                                    |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                    |
| sqlglot_optimize        | 52.7 ms                                                | 50.9 ms: 1.04x faster                                                     |
| tornado_http            | 96.5 ms                                                | 93.4 ms: 1.03x faster                                                     |
| dulwich_log             | 64.0 ms                                                | 62.0 ms: 1.03x faster                                                     |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                      |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                      |
| thrift                  | 760 us                                                 | 738 us: 1.03x faster                                                      |
| telco                   | 6.43 ms                                                | 6.26 ms: 1.03x faster                                                     |
| pidigits                | 197 ms                                                 | 192 ms: 1.02x faster                                                      |
| coverage                | 99.3 ms                                                | 97.0 ms: 1.02x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                                     |
| logging_format          | 6.48 us                                                | 6.36 us: 1.02x faster                                                     |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| mako                    | 9.83 ms                                                | 9.70 ms: 1.01x faster                                                     |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                                      |
| chameleon               | 6.38 ms                                                | 6.42 ms: 1.01x slower                                                     |
| regex_v8                | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                     |
| xml_etree_process       | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                     |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                      |
| pickle_dict             | 31.2 us                                                | 31.9 us: 1.02x slower                                                     |
| mdp                     | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                    |
| xml_etree_generate      | 75.9 ms                                                | 77.9 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed | 736 ms                                                 | 757 ms: 1.03x slower                                                      |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                      |
| pickle_list             | 4.14 us                                                | 4.27 us: 1.03x slower                                                     |
| nbody                   | 90.0 ms                                                | 92.8 ms: 1.03x slower                                                     |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                     |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                     |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                                     |
| python_startup          | 8.58 ms                                                | 8.96 ms: 1.04x slower                                                     |
| generators              | 73.5 ms                                                | 76.9 ms: 1.05x slower                                                     |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                     |
| regex_effbot            | 3.46 ms                                                | 3.64 ms: 1.05x slower                                                     |
| python_startup_no_site  | 6.04 ms                                                | 6.48 ms: 1.07x slower                                                     |
| gc_traversal            | 3.82 ms                                                | 4.30 ms: 1.13x slower                                                     |
| dask                    | 365 ms                                                 | 495 ms: 1.36x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (10): spectral_norm, async_tree_none, async_generators, bench_mp_pool, django_template, async_tree_memoization, pathlib, djangocms, unpickle_list, unpickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-b1845b6/bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6.json: mypy
