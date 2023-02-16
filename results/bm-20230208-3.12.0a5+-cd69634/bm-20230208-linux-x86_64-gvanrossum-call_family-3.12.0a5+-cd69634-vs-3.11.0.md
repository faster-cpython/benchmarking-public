
# Results vs. 3.11.0

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: cd69634
- commit date: 2023-02-08
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                              |
| chameleon      | 6.38 ms                                                | 6.44 ms: 1.01x slower                                             |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                            |
| html5lib       | 64.8 ms                                                | 60.7 ms: 1.07x faster                                             |
| tornado_http   | 96.5 ms                                                | 94.3 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                              |
| float          | 76.8 ms                                                | 74.0 ms: 1.04x faster                                             |
| nbody          | 90.0 ms                                                | 94.6 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.0 ms: 1.06x faster                                             |
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                              |
| regex_dna      | 203 ms                                                 | 206 ms: 1.01x slower                                              |
| regex_effbot   | 3.46 ms                                                | 3.64 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.44 ms: 1.31x faster                                             |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                              |
| xml_etree_parse      | 160 ms                                                 | 146 ms: 1.10x faster                                              |
| json_loads           | 26.1 us                                                | 23.8 us: 1.09x faster                                             |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                              |
| pickle_list          | 4.14 us                                                | 4.03 us: 1.03x faster                                             |
| pickle_dict          | 31.2 us                                                | 30.3 us: 1.03x faster                                             |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                              |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                             |
| xml_etree_process    | 53.7 ms                                                | 53.2 ms: 1.01x faster                                             |
| xml_etree_generate   | 75.9 ms                                                | 77.1 ms: 1.02x slower                                             |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                             |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.91 ms: 1.04x slower                                             |
| python_startup_no_site | 6.04 ms                                                | 6.47 ms: 1.07x slower                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.1 ms: 1.09x faster                                             |
| genshi_text     | 21.5 ms                                                | 20.5 ms: 1.05x faster                                             |
| mako            | 9.83 ms                                                | 9.97 ms: 1.01x slower                                             |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 490 ms: 1.80x faster                                              |
| json_dumps              | 12.4 ms                                                | 9.44 ms: 1.31x faster                                             |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                              |
| deltablue               | 3.66 ms                                                | 3.17 ms: 1.15x faster                                             |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.01 ms: 1.14x faster                                             |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                              |
| xml_etree_parse         | 160 ms                                                 | 146 ms: 1.10x faster                                              |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                              |
| json_loads              | 26.1 us                                                | 23.8 us: 1.09x faster                                             |
| genshi_xml              | 51.4 ms                                                | 47.1 ms: 1.09x faster                                             |
| richards                | 46.1 ms                                                | 42.3 ms: 1.09x faster                                             |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                            |
| fannkuch                | 384 ms                                                 | 356 ms: 1.08x faster                                              |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                              |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                              |
| coroutines              | 26.2 ms                                                | 24.3 ms: 1.08x faster                                             |
| html5lib                | 64.8 ms                                                | 60.7 ms: 1.07x faster                                             |
| scimark_fft             | 325 ms                                                 | 305 ms: 1.07x faster                                              |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                              |
| regex_v8                | 22.2 ms                                                | 21.0 ms: 1.06x faster                                             |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                             |
| mdp                     | 2.63 sec                                               | 2.48 sec: 1.06x faster                                            |
| nqueens                 | 83.8 ms                                                | 79.2 ms: 1.06x faster                                             |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                              |
| hexiom                  | 6.34 ms                                                | 6.02 ms: 1.05x faster                                             |
| json                    | 4.87 ms                                                | 4.64 ms: 1.05x faster                                             |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                             |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                              |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                             |
| bench_thread_pool       | 817 us                                                 | 783 us: 1.04x faster                                              |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                              |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                            |
| crypto_pyaes            | 75.7 ms                                                | 72.7 ms: 1.04x faster                                             |
| float                   | 76.8 ms                                                | 74.0 ms: 1.04x faster                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                             |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                             |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                              |
| scimark_monte_carlo     | 68.0 ms                                                | 65.8 ms: 1.03x faster                                             |
| chaos                   | 68.7 ms                                                | 66.7 ms: 1.03x faster                                             |
| pyflate                 | 419 ms                                                 | 407 ms: 1.03x faster                                              |
| pickle_list             | 4.14 us                                                | 4.03 us: 1.03x faster                                             |
| deepcopy                | 341 us                                                 | 332 us: 1.03x faster                                              |
| async_generators        | 356 ms                                                 | 346 ms: 1.03x faster                                              |
| pickle_dict             | 31.2 us                                                | 30.3 us: 1.03x faster                                             |
| thrift                  | 760 us                                                 | 740 us: 1.03x faster                                              |
| sqlglot_optimize        | 52.7 ms                                                | 51.4 ms: 1.03x faster                                             |
| deepcopy_memo           | 35.8 us                                                | 34.9 us: 1.03x faster                                             |
| logging_simple          | 6.02 us                                                | 5.88 us: 1.02x faster                                             |
| tornado_http            | 96.5 ms                                                | 94.3 ms: 1.02x faster                                             |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                              |
| spectral_norm           | 98.1 ms                                                | 96.1 ms: 1.02x faster                                             |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                            |
| generators              | 73.5 ms                                                | 72.1 ms: 1.02x faster                                             |
| deepcopy_reduce         | 3.02 us                                                | 2.96 us: 1.02x faster                                             |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                              |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                             |
| logging_silent          | 98.0 ns                                                | 96.3 ns: 1.02x faster                                             |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                              |
| pprint_safe_repr        | 706 ms                                                 | 697 ms: 1.01x faster                                              |
| raytrace                | 291 ms                                                 | 288 ms: 1.01x faster                                              |
| telco                   | 6.43 ms                                                | 6.36 ms: 1.01x faster                                             |
| dulwich_log             | 64.0 ms                                                | 63.4 ms: 1.01x faster                                             |
| xml_etree_process       | 53.7 ms                                                | 53.2 ms: 1.01x faster                                             |
| coverage                | 99.3 ms                                                | 98.8 ms: 1.00x faster                                             |
| chameleon               | 6.38 ms                                                | 6.44 ms: 1.01x slower                                             |
| regex_dna               | 203 ms                                                 | 206 ms: 1.01x slower                                              |
| mako                    | 9.83 ms                                                | 9.97 ms: 1.01x slower                                             |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                            |
| xml_etree_generate      | 75.9 ms                                                | 77.1 ms: 1.02x slower                                             |
| async_tree_memoization  | 624 ms                                                 | 637 ms: 1.02x slower                                              |
| meteor_contest          | 104 ms                                                 | 107 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed | 736 ms                                                 | 752 ms: 1.02x slower                                              |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                             |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                             |
| python_startup          | 8.58 ms                                                | 8.91 ms: 1.04x slower                                             |
| sqlite_synth            | 2.48 us                                                | 2.60 us: 1.05x slower                                             |
| nbody                   | 90.0 ms                                                | 94.6 ms: 1.05x slower                                             |
| regex_effbot            | 3.46 ms                                                | 3.64 ms: 1.05x slower                                             |
| sqlglot_transpile       | 1.65 ms                                                | 1.74 ms: 1.05x slower                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.06x slower                                             |
| python_startup_no_site  | 6.04 ms                                                | 6.47 ms: 1.07x slower                                             |
| gc_traversal            | 3.82 ms                                                | 4.17 ms: 1.09x slower                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (10): djangocms, sqlalchemy_declarative, pathlib, async_tree_none, unpickle_list, logging_format, unpack_sequence, bench_mp_pool, sqlalchemy_imperative, scimark_lu
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
