
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 1f6d134
- commit date: 2023-02-07
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                         |
| chameleon      | 6.41 ms                                                | 6.58 ms: 1.03x slower                                                        |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| html5lib       | 63.2 ms                                                | 61.3 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                                         |
| float          | 76.3 ms                                                | 74.0 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                         |
| regex_v8       | 22.3 ms                                                | 21.7 ms: 1.03x faster                                                        |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                         |
| regex_effbot   | 3.36 ms                                                | 3.76 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.47 ms: 1.34x faster                                                        |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                                         |
| json_loads           | 26.2 us                                                | 23.8 us: 1.10x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| pickle_dict          | 31.4 us                                                | 30.0 us: 1.05x faster                                                        |
| pickle_pure_python   | 304 us                                                 | 292 us: 1.04x faster                                                         |
| pickle_list          | 4.17 us                                                | 4.05 us: 1.03x faster                                                        |
| pickle               | 9.79 us                                                | 9.96 us: 1.02x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.6 ms: 1.02x slower                                                        |
| unpickle_list        | 4.95 us                                                | 5.04 us: 1.02x slower                                                        |
| unpickle             | 13.3 us                                                | 14.1 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.94 ms: 1.07x slower                                                        |
| python_startup_no_site | 5.96 ms                                                | 6.45 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.3 ms: 1.10x faster                                                        |
| genshi_text     | 22.1 ms                                                | 21.0 ms: 1.05x faster                                                        |
| mako            | 9.85 ms                                                | 9.98 ms: 1.01x slower                                                        |
| django_template | 32.5 ms                                                | 33.2 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.47 ms: 1.34x faster                                                        |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                                         |
| nqueens                 | 85.0 ms                                                | 76.5 ms: 1.11x faster                                                        |
| json_loads              | 26.2 us                                                | 23.8 us: 1.10x faster                                                        |
| genshi_xml              | 52.1 ms                                                | 47.3 ms: 1.10x faster                                                        |
| deltablue               | 3.64 ms                                                | 3.35 ms: 1.09x faster                                                        |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| pycparser               | 1.17 sec                                               | 1.09 sec: 1.07x faster                                                       |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.11 ms: 1.07x faster                                                        |
| fannkuch                | 388 ms                                                 | 365 ms: 1.06x faster                                                         |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                         |
| mdp                     | 2.62 sec                                               | 2.48 sec: 1.06x faster                                                       |
| spectral_norm           | 99.9 ms                                                | 94.6 ms: 1.06x faster                                                        |
| scimark_fft             | 329 ms                                                 | 312 ms: 1.06x faster                                                         |
| hexiom                  | 6.35 ms                                                | 6.02 ms: 1.05x faster                                                        |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                                         |
| sympy_sum               | 166 ms                                                 | 157 ms: 1.05x faster                                                         |
| genshi_text             | 22.1 ms                                                | 21.0 ms: 1.05x faster                                                        |
| logging_simple          | 6.06 us                                                | 5.78 us: 1.05x faster                                                        |
| sympy_str               | 287 ms                                                 | 274 ms: 1.05x faster                                                         |
| pickle_dict             | 31.4 us                                                | 30.0 us: 1.05x faster                                                        |
| sympy_integrate         | 20.9 ms                                                | 20.0 ms: 1.04x faster                                                        |
| chaos                   | 68.6 ms                                                | 65.9 ms: 1.04x faster                                                        |
| pickle_pure_python      | 304 us                                                 | 292 us: 1.04x faster                                                         |
| scimark_monte_carlo     | 68.3 ms                                                | 65.8 ms: 1.04x faster                                                        |
| richards                | 46.2 ms                                                | 44.6 ms: 1.04x faster                                                        |
| telco                   | 6.62 ms                                                | 6.40 ms: 1.04x faster                                                        |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                         |
| json                    | 4.95 ms                                                | 4.79 ms: 1.03x faster                                                        |
| coroutines              | 26.1 ms                                                | 25.3 ms: 1.03x faster                                                        |
| float                   | 76.3 ms                                                | 74.0 ms: 1.03x faster                                                        |
| html5lib                | 63.2 ms                                                | 61.3 ms: 1.03x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 1.02 ms: 1.03x faster                                                        |
| pickle_list             | 4.17 us                                                | 4.05 us: 1.03x faster                                                        |
| pprint_pformat          | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                       |
| regex_v8                | 22.3 ms                                                | 21.7 ms: 1.03x faster                                                        |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| go                      | 143 ms                                                 | 140 ms: 1.03x faster                                                         |
| logging_format          | 6.62 us                                                | 6.46 us: 1.03x faster                                                        |
| deepcopy_memo           | 36.4 us                                                | 35.7 us: 1.02x faster                                                        |
| sqlglot_optimize        | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.10 ms: 1.02x faster                                                        |
| bench_thread_pool       | 810 us                                                 | 795 us: 1.02x faster                                                         |
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                         |
| async_generators        | 359 ms                                                 | 354 ms: 1.01x faster                                                         |
| coverage                | 101 ms                                                 | 99.2 ms: 1.01x faster                                                        |
| pyflate                 | 417 ms                                                 | 412 ms: 1.01x faster                                                         |
| sqlalchemy_imperative   | 18.0 ms                                                | 17.8 ms: 1.01x faster                                                        |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                        |
| thrift                  | 752 us                                                 | 745 us: 1.01x faster                                                         |
| pprint_safe_repr        | 691 ms                                                 | 684 ms: 1.01x faster                                                         |
| raytrace                | 290 ms                                                 | 288 ms: 1.01x faster                                                         |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 108 ms: 1.00x faster                                                         |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                       |
| dulwich_log             | 63.9 ms                                                | 64.5 ms: 1.01x slower                                                        |
| mako                    | 9.85 ms                                                | 9.98 ms: 1.01x slower                                                        |
| deepcopy_reduce         | 2.97 us                                                | 3.01 us: 1.01x slower                                                        |
| logging_silent          | 98.5 ns                                                | 99.9 ns: 1.01x slower                                                        |
| pickle                  | 9.79 us                                                | 9.96 us: 1.02x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 77.6 ms: 1.02x slower                                                        |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                         |
| unpickle_list           | 4.95 us                                                | 5.04 us: 1.02x slower                                                        |
| unpack_sequence         | 43.4 ns                                                | 44.2 ns: 1.02x slower                                                        |
| django_template         | 32.5 ms                                                | 33.2 ms: 1.02x slower                                                        |
| chameleon               | 6.41 ms                                                | 6.58 ms: 1.03x slower                                                        |
| scimark_lu              | 107 ms                                                 | 111 ms: 1.03x slower                                                         |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                                        |
| sqlglot_transpile       | 1.66 ms                                                | 1.74 ms: 1.05x slower                                                        |
| sqlglot_parse           | 1.37 ms                                                | 1.45 ms: 1.06x slower                                                        |
| unpickle                | 13.3 us                                                | 14.1 us: 1.06x slower                                                        |
| async_tree_memoization  | 625 ms                                                 | 664 ms: 1.06x slower                                                         |
| python_startup          | 8.36 ms                                                | 8.94 ms: 1.07x slower                                                        |
| python_startup_no_site  | 5.96 ms                                                | 6.45 ms: 1.08x slower                                                        |
| generators              | 72.2 ms                                                | 78.6 ms: 1.09x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.76 ms: 1.12x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (10): async_tree_none, sqlalchemy_declarative, tornado_http, crypto_pyaes, deepcopy, xml_etree_iterparse, bench_mp_pool, xml_etree_process, async_tree_cpu_io_mixed, nbody
Ignored benchmarks (3) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy, pylint
Ignored benchmarks (6) of /home/mdboom/Work/builds/benchmarking/results/bm-20230207-3.12.0a4+-1f6d134/bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
