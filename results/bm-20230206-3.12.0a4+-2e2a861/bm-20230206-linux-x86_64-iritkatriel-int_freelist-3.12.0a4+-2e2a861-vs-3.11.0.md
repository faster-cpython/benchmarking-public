
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 2e2a861
- commit date: 2023-02-06
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.35 ms: 1.01x faster                                               |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                              |
| html5lib       | 63.2 ms                                                | 60.3 ms: 1.05x faster                                               |
| tornado_http   | 96.6 ms                                                | 93.9 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 73.2 ms: 1.04x faster                                               |
| nbody          | 95.0 ms                                                | 95.9 ms: 1.01x slower                                               |
| pidigits       | 199 ms                                                 | 203 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                |
| regex_v8       | 22.3 ms                                                | 22.4 ms: 1.00x slower                                               |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                |
| regex_effbot   | 3.36 ms                                                | 3.51 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.34 ms: 1.36x faster                                               |
| unpickle_pure_python | 225 us                                                 | 200 us: 1.13x faster                                                |
| json_loads           | 26.2 us                                                | 23.5 us: 1.11x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.07x faster                                                |
| pickle_pure_python   | 304 us                                                 | 285 us: 1.07x faster                                                |
| xml_etree_process    | 53.8 ms                                                | 53.4 ms: 1.01x faster                                               |
| pickle_dict          | 31.4 us                                                | 31.5 us: 1.00x slower                                               |
| pickle_list          | 4.17 us                                                | 4.22 us: 1.01x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                               |
| pickle               | 9.79 us                                                | 10.1 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.96 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.49 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 46.5 ms: 1.12x faster                                               |
| genshi_text    | 22.1 ms                                                | 20.7 ms: 1.07x faster                                               |
| mako           | 9.85 ms                                                | 9.46 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.34 ms: 1.36x faster                                               |
| deltablue               | 3.64 ms                                                | 3.21 ms: 1.13x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 200 us: 1.13x faster                                                |
| genshi_xml              | 52.1 ms                                                | 46.5 ms: 1.12x faster                                               |
| json_loads              | 26.2 us                                                | 23.5 us: 1.11x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.96 ms: 1.11x faster                                               |
| json                    | 4.95 ms                                                | 4.50 ms: 1.10x faster                                               |
| scimark_fft             | 329 ms                                                 | 302 ms: 1.09x faster                                                |
| nqueens                 | 85.0 ms                                                | 78.1 ms: 1.09x faster                                               |
| richards                | 46.2 ms                                                | 42.6 ms: 1.08x faster                                               |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.07x faster                                                |
| telco                   | 6.62 ms                                                | 6.17 ms: 1.07x faster                                               |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                |
| logging_silent          | 98.5 ns                                                | 92.2 ns: 1.07x faster                                               |
| genshi_text             | 22.1 ms                                                | 20.7 ms: 1.07x faster                                               |
| logging_simple          | 6.06 us                                                | 5.69 us: 1.07x faster                                               |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                |
| sympy_str               | 287 ms                                                 | 270 ms: 1.07x faster                                                |
| pickle_pure_python      | 304 us                                                 | 285 us: 1.07x faster                                                |
| coroutines              | 26.1 ms                                                | 24.5 ms: 1.06x faster                                               |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                               |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                |
| pprint_pformat          | 1.44 sec                                               | 1.36 sec: 1.06x faster                                              |
| chaos                   | 68.6 ms                                                | 64.9 ms: 1.06x faster                                               |
| pyflate                 | 417 ms                                                 | 395 ms: 1.06x faster                                                |
| hexiom                  | 6.35 ms                                                | 6.02 ms: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                | 994 us: 1.05x faster                                                |
| deepcopy_memo           | 36.4 us                                                | 34.7 us: 1.05x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                               |
| logging_format          | 6.62 us                                                | 6.32 us: 1.05x faster                                               |
| spectral_norm           | 99.9 ms                                                | 95.5 ms: 1.05x faster                                               |
| html5lib                | 63.2 ms                                                | 60.3 ms: 1.05x faster                                               |
| float                   | 76.3 ms                                                | 73.2 ms: 1.04x faster                                               |
| mako                    | 9.85 ms                                                | 9.46 ms: 1.04x faster                                               |
| sqlglot_optimize        | 53.0 ms                                                | 50.9 ms: 1.04x faster                                               |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                              |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                               |
| bench_thread_pool       | 810 us                                                 | 779 us: 1.04x faster                                                |
| coverage                | 101 ms                                                 | 96.8 ms: 1.04x faster                                               |
| pprint_safe_repr        | 691 ms                                                 | 666 ms: 1.04x faster                                                |
| sympy_expand            | 472 ms                                                 | 456 ms: 1.04x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| deepcopy                | 344 us                                                 | 334 us: 1.03x faster                                                |
| tornado_http            | 96.6 ms                                                | 93.9 ms: 1.03x faster                                               |
| pycparser               | 1.17 sec                                               | 1.14 sec: 1.03x faster                                              |
| scimark_monte_carlo     | 68.3 ms                                                | 66.6 ms: 1.02x faster                                               |
| dulwich_log             | 63.9 ms                                                | 62.4 ms: 1.02x faster                                               |
| raytrace                | 290 ms                                                 | 284 ms: 1.02x faster                                                |
| async_generators        | 359 ms                                                 | 352 ms: 1.02x faster                                                |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| thrift                  | 752 us                                                 | 740 us: 1.02x faster                                                |
| unpack_sequence         | 43.4 ns                                                | 42.8 ns: 1.01x faster                                               |
| scimark_lu              | 107 ms                                                 | 106 ms: 1.01x faster                                                |
| chameleon               | 6.41 ms                                                | 6.35 ms: 1.01x faster                                               |
| xml_etree_process       | 53.8 ms                                                | 53.4 ms: 1.01x faster                                               |
| pickle_dict             | 31.4 us                                                | 31.5 us: 1.00x slower                                               |
| regex_v8                | 22.3 ms                                                | 22.4 ms: 1.00x slower                                               |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 752 ms                                                 | 757 ms: 1.01x slower                                                |
| nbody                   | 95.0 ms                                                | 95.9 ms: 1.01x slower                                               |
| pickle_list             | 4.17 us                                                | 4.22 us: 1.01x slower                                               |
| mdp                     | 2.62 sec                                               | 2.65 sec: 1.01x slower                                              |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                               |
| pidigits                | 199 ms                                                 | 203 ms: 1.02x slower                                                |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                               |
| crypto_pyaes            | 73.9 ms                                                | 75.7 ms: 1.02x slower                                               |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.03x slower                                               |
| pickle                  | 9.79 us                                                | 10.1 us: 1.04x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.51 ms: 1.04x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.61 us: 1.05x slower                                               |
| python_startup          | 8.36 ms                                                | 8.96 ms: 1.07x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.49 ms: 1.09x slower                                               |
| generators              | 72.2 ms                                                | 78.7 ms: 1.09x slower                                               |
| mypy                    | 669 ms                                                 | 806 ms: 1.21x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (9): unpickle, async_tree_none, async_tree_memoization, meteor_contest, bench_mp_pool, django_template, xml_etree_iterparse, deepcopy_reduce, unpickle_list
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230206-3.12.0a4+-2e2a861/bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
