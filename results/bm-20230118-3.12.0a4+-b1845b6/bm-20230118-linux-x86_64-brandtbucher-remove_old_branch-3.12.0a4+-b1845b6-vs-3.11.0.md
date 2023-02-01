
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
| 2to3           | 257 ms                                                 | 251 ms: 1.02x faster                                                      |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                    |
| html5lib       | 63.2 ms                                                | 59.6 ms: 1.06x faster                                                     |
| tornado_http   | 96.6 ms                                                | 93.4 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.5 ms: 1.05x faster                                                     |
| pidigits       | 199 ms                                                 | 192 ms: 1.04x faster                                                      |
| nbody          | 95.0 ms                                                | 92.8 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                      |
| regex_v8       | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                     |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                      |
| regex_effbot   | 3.36 ms                                                | 3.64 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.42 ms: 1.34x faster                                                     |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                                      |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                                     |
| pickle_pure_python   | 304 us                                                 | 285 us: 1.07x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.04x faster                                                      |
| xml_etree_process    | 53.8 ms                                                | 54.1 ms: 1.01x slower                                                     |
| unpickle_list        | 4.95 us                                                | 5.01 us: 1.01x slower                                                     |
| pickle_dict          | 31.4 us                                                | 31.9 us: 1.01x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 77.9 ms: 1.02x slower                                                     |
| pickle_list          | 4.17 us                                                | 4.27 us: 1.02x slower                                                     |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.03x slower                                                      |
| pickle               | 9.79 us                                                | 10.2 us: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.96 ms: 1.07x slower                                                     |
| python_startup_no_site | 5.96 ms                                                | 6.48 ms: 1.09x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 47.0 ms: 1.11x faster                                                     |
| genshi_text    | 22.1 ms                                                | 20.6 ms: 1.07x faster                                                     |
| mako           | 9.85 ms                                                | 9.70 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.42 ms: 1.34x faster                                                     |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                                      |
| deltablue               | 3.64 ms                                                | 3.22 ms: 1.13x faster                                                     |
| nqueens                 | 85.0 ms                                                | 76.7 ms: 1.11x faster                                                     |
| genshi_xml              | 52.1 ms                                                | 47.0 ms: 1.11x faster                                                     |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                                     |
| richards                | 46.2 ms                                                | 42.1 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.04 ms: 1.09x faster                                                     |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                      |
| scimark_fft             | 329 ms                                                 | 303 ms: 1.09x faster                                                      |
| go                      | 143 ms                                                 | 133 ms: 1.08x faster                                                      |
| json                    | 4.95 ms                                                | 4.59 ms: 1.08x faster                                                     |
| deepcopy_memo           | 36.4 us                                                | 33.9 us: 1.08x faster                                                     |
| logging_silent          | 98.5 ns                                                | 91.6 ns: 1.08x faster                                                     |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                      |
| sympy_str               | 287 ms                                                 | 268 ms: 1.07x faster                                                      |
| genshi_text             | 22.1 ms                                                | 20.6 ms: 1.07x faster                                                     |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                      |
| pickle_pure_python      | 304 us                                                 | 285 us: 1.07x faster                                                      |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                      |
| chaos                   | 68.6 ms                                                | 64.3 ms: 1.07x faster                                                     |
| sympy_integrate         | 20.9 ms                                                | 19.6 ms: 1.06x faster                                                     |
| html5lib                | 63.2 ms                                                | 59.6 ms: 1.06x faster                                                     |
| telco                   | 6.62 ms                                                | 6.26 ms: 1.06x faster                                                     |
| deepcopy                | 344 us                                                 | 326 us: 1.06x faster                                                      |
| hexiom                  | 6.35 ms                                                | 6.02 ms: 1.05x faster                                                     |
| logging_simple          | 6.06 us                                                | 5.76 us: 1.05x faster                                                     |
| float                   | 76.3 ms                                                | 72.5 ms: 1.05x faster                                                     |
| coroutines              | 26.1 ms                                                | 24.8 ms: 1.05x faster                                                     |
| aiohttp                 | 1.05 ms                                                | 996 us: 1.05x faster                                                      |
| pyflate                 | 417 ms                                                 | 397 ms: 1.05x faster                                                      |
| scimark_monte_carlo     | 68.3 ms                                                | 65.1 ms: 1.05x faster                                                     |
| bench_thread_pool       | 810 us                                                 | 774 us: 1.05x faster                                                      |
| sympy_expand            | 472 ms                                                 | 451 ms: 1.05x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                                     |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.04x faster                                                      |
| sqlglot_optimize        | 53.0 ms                                                | 50.9 ms: 1.04x faster                                                     |
| unpack_sequence         | 43.4 ns                                                | 41.7 ns: 1.04x faster                                                     |
| logging_format          | 6.62 us                                                | 6.36 us: 1.04x faster                                                     |
| pidigits                | 199 ms                                                 | 192 ms: 1.04x faster                                                      |
| coverage                | 101 ms                                                 | 97.0 ms: 1.04x faster                                                     |
| tornado_http            | 96.6 ms                                                | 93.4 ms: 1.03x faster                                                     |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                    |
| pprint_pformat          | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                    |
| dulwich_log             | 63.9 ms                                                | 62.0 ms: 1.03x faster                                                     |
| raytrace                | 290 ms                                                 | 283 ms: 1.03x faster                                                      |
| pycparser               | 1.17 sec                                               | 1.14 sec: 1.03x faster                                                    |
| nbody                   | 95.0 ms                                                | 92.8 ms: 1.02x faster                                                     |
| 2to3                    | 257 ms                                                 | 251 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                      |
| spectral_norm           | 99.9 ms                                                | 97.6 ms: 1.02x faster                                                     |
| pprint_safe_repr        | 691 ms                                                 | 676 ms: 1.02x faster                                                      |
| deepcopy_reduce         | 2.97 us                                                | 2.91 us: 1.02x faster                                                     |
| thrift                  | 752 us                                                 | 738 us: 1.02x faster                                                      |
| crypto_pyaes            | 73.9 ms                                                | 72.6 ms: 1.02x faster                                                     |
| mako                    | 9.85 ms                                                | 9.70 ms: 1.01x faster                                                     |
| async_generators        | 359 ms                                                 | 355 ms: 1.01x faster                                                      |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                      |
| scimark_lu              | 107 ms                                                 | 106 ms: 1.01x faster                                                      |
| regex_v8                | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                     |
| xml_etree_process       | 53.8 ms                                                | 54.1 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed | 752 ms                                                 | 757 ms: 1.01x slower                                                      |
| unpickle_list           | 4.95 us                                                | 5.01 us: 1.01x slower                                                     |
| pickle_dict             | 31.4 us                                                | 31.9 us: 1.01x slower                                                     |
| xml_etree_generate      | 76.2 ms                                                | 77.9 ms: 1.02x slower                                                     |
| pickle_list             | 4.17 us                                                | 4.27 us: 1.02x slower                                                     |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.03x slower                                                     |
| mdp                     | 2.62 sec                                               | 2.69 sec: 1.03x slower                                                    |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.42 ms: 1.03x slower                                                     |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.03x slower                                                      |
| pickle                  | 9.79 us                                                | 10.2 us: 1.05x slower                                                     |
| sqlite_synth            | 2.49 us                                                | 2.61 us: 1.05x slower                                                     |
| generators              | 72.2 ms                                                | 76.9 ms: 1.07x slower                                                     |
| python_startup          | 8.36 ms                                                | 8.96 ms: 1.07x slower                                                     |
| regex_effbot            | 3.36 ms                                                | 3.64 ms: 1.08x slower                                                     |
| python_startup_no_site  | 5.96 ms                                                | 6.48 ms: 1.09x slower                                                     |
| mypy                    | 669 ms                                                 | 805 ms: 1.20x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (8): async_tree_none, django_template, pathlib, bench_mp_pool, async_tree_memoization, chameleon, async_tree_io, unpickle
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-b1845b6/bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
