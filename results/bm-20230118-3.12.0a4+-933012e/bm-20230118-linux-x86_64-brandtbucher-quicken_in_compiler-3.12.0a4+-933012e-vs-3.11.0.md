
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 933012e
- commit date: 2023-01-18
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 249 ms: 1.03x faster                                                        |
| chameleon      | 6.41 ms                                                | 6.37 ms: 1.01x faster                                                       |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                      |
| html5lib       | 63.2 ms                                                | 59.8 ms: 1.06x faster                                                       |
| tornado_http   | 96.6 ms                                                | 94.3 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.3 ms: 1.06x faster                                                       |
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                                        |
| nbody          | 95.0 ms                                                | 94.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                        |
| regex_v8       | 22.3 ms                                                | 21.2 ms: 1.05x faster                                                       |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| regex_effbot   | 3.36 ms                                                | 3.51 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.32 ms: 1.36x faster                                                       |
| unpickle_pure_python | 225 us                                                 | 196 us: 1.15x faster                                                        |
| json_loads           | 26.2 us                                                | 24.1 us: 1.09x faster                                                       |
| pickle_pure_python   | 304 us                                                 | 280 us: 1.09x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                        |
| xml_etree_process    | 53.8 ms                                                | 54.1 ms: 1.01x slower                                                       |
| pickle_dict          | 31.4 us                                                | 31.6 us: 1.01x slower                                                       |
| pickle_list          | 4.17 us                                                | 4.21 us: 1.01x slower                                                       |
| unpickle_list        | 4.95 us                                                | 5.09 us: 1.03x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 78.5 ms: 1.03x slower                                                       |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                                       |
| unpickle             | 13.3 us                                                | 14.0 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.85 ms: 1.06x slower                                                       |
| python_startup_no_site | 5.96 ms                                                | 6.39 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.0 ms: 1.13x faster                                                       |
| genshi_text     | 22.1 ms                                                | 20.0 ms: 1.10x faster                                                       |
| mako            | 9.85 ms                                                | 9.50 ms: 1.04x faster                                                       |
| django_template | 32.5 ms                                                | 32.3 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.32 ms: 1.36x faster                                                       |
| unpickle_pure_python    | 225 us                                                 | 196 us: 1.15x faster                                                        |
| deltablue               | 3.64 ms                                                | 3.20 ms: 1.14x faster                                                       |
| genshi_xml              | 52.1 ms                                                | 46.0 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.96 ms: 1.11x faster                                                       |
| genshi_text             | 22.1 ms                                                | 20.0 ms: 1.10x faster                                                       |
| nqueens                 | 85.0 ms                                                | 77.2 ms: 1.10x faster                                                       |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                                        |
| richards                | 46.2 ms                                                | 42.2 ms: 1.09x faster                                                       |
| scimark_fft             | 329 ms                                                 | 301 ms: 1.09x faster                                                        |
| logging_silent          | 98.5 ns                                                | 90.4 ns: 1.09x faster                                                       |
| json_loads              | 26.2 us                                                | 24.1 us: 1.09x faster                                                       |
| pickle_pure_python      | 304 us                                                 | 280 us: 1.09x faster                                                        |
| pycparser               | 1.17 sec                                               | 1.08 sec: 1.09x faster                                                      |
| chaos                   | 68.6 ms                                                | 63.3 ms: 1.08x faster                                                       |
| logging_simple          | 6.06 us                                                | 5.62 us: 1.08x faster                                                       |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.44 sec: 1.07x faster                                                      |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                        |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                        |
| logging_format          | 6.62 us                                                | 6.18 us: 1.07x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                        |
| json                    | 4.95 ms                                                | 4.64 ms: 1.07x faster                                                       |
| hexiom                  | 6.35 ms                                                | 5.96 ms: 1.06x faster                                                       |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                        |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                        |
| deepcopy_memo           | 36.4 us                                                | 34.4 us: 1.06x faster                                                       |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.06x faster                                                       |
| deepcopy                | 344 us                                                 | 325 us: 1.06x faster                                                        |
| html5lib                | 63.2 ms                                                | 59.8 ms: 1.06x faster                                                       |
| float                   | 76.3 ms                                                | 72.3 ms: 1.06x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 991 us: 1.06x faster                                                        |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                                        |
| regex_v8                | 22.3 ms                                                | 21.2 ms: 1.05x faster                                                       |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                      |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                      |
| coverage                | 101 ms                                                 | 96.1 ms: 1.05x faster                                                       |
| pyflate                 | 417 ms                                                 | 399 ms: 1.05x faster                                                        |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                                        |
| bench_thread_pool       | 810 us                                                 | 779 us: 1.04x faster                                                        |
| mako                    | 9.85 ms                                                | 9.50 ms: 1.04x faster                                                       |
| scimark_monte_carlo     | 68.3 ms                                                | 65.9 ms: 1.04x faster                                                       |
| 2to3                    | 257 ms                                                 | 249 ms: 1.03x faster                                                        |
| telco                   | 6.62 ms                                                | 6.42 ms: 1.03x faster                                                       |
| pprint_safe_repr        | 691 ms                                                 | 670 ms: 1.03x faster                                                        |
| sqlglot_optimize        | 53.0 ms                                                | 51.4 ms: 1.03x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                       |
| async_generators        | 359 ms                                                 | 349 ms: 1.03x faster                                                        |
| raytrace                | 290 ms                                                 | 283 ms: 1.03x faster                                                        |
| spectral_norm           | 99.9 ms                                                | 97.4 ms: 1.03x faster                                                       |
| tornado_http            | 96.6 ms                                                | 94.3 ms: 1.03x faster                                                       |
| scimark_lu              | 107 ms                                                 | 106 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                | 2.92 us: 1.02x faster                                                       |
| thrift                  | 752 us                                                 | 739 us: 1.02x faster                                                        |
| meteor_contest          | 105 ms                                                 | 103 ms: 1.02x faster                                                        |
| dulwich_log             | 63.9 ms                                                | 62.9 ms: 1.02x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                        |
| nbody                   | 95.0 ms                                                | 94.1 ms: 1.01x faster                                                       |
| django_template         | 32.5 ms                                                | 32.3 ms: 1.01x faster                                                       |
| chameleon               | 6.41 ms                                                | 6.37 ms: 1.01x faster                                                       |
| xml_etree_process       | 53.8 ms                                                | 54.1 ms: 1.01x slower                                                       |
| pickle_dict             | 31.4 us                                                | 31.6 us: 1.01x slower                                                       |
| pickle_list             | 4.17 us                                                | 4.21 us: 1.01x slower                                                       |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                      |
| unpack_sequence         | 43.4 ns                                                | 44.0 ns: 1.01x slower                                                       |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.02x slower                                                       |
| async_tree_memoization  | 625 ms                                                 | 639 ms: 1.02x slower                                                        |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                       |
| unpickle_list           | 4.95 us                                                | 5.09 us: 1.03x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 78.5 ms: 1.03x slower                                                       |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                                       |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                                       |
| regex_effbot            | 3.36 ms                                                | 3.51 ms: 1.05x slower                                                       |
| unpickle                | 13.3 us                                                | 14.0 us: 1.05x slower                                                       |
| generators              | 72.2 ms                                                | 76.0 ms: 1.05x slower                                                       |
| python_startup          | 8.36 ms                                                | 8.85 ms: 1.06x slower                                                       |
| python_startup_no_site  | 5.96 ms                                                | 6.39 ms: 1.07x slower                                                       |
| mypy                    | 669 ms                                                 | 804 ms: 1.20x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (6): async_tree_none, coroutines, xml_etree_iterparse, async_tree_cpu_io_mixed, bench_mp_pool, crypto_pyaes
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230118-3.12.0a4+-933012e/bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
