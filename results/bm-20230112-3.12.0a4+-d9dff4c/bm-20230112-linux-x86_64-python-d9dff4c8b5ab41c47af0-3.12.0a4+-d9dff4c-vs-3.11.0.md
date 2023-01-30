
# Results vs. 3.11.0

- fork: python
- ref: d9dff4c8b5ab41c47af0
- machine: linux-x86_64
- commit hash: d9dff4c
- commit date: 2023-01-12
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                   |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                 |
| html5lib       | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.4 ms: 1.05x faster                                                  |
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                                   |
| regex_v8       | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                  |
| regex_dna      | 203 ms                                                 | 206 ms: 1.01x slower                                                   |
| regex_effbot   | 3.36 ms                                                | 3.61 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.39 ms: 1.35x faster                                                  |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                   |
| json_loads           | 26.2 us                                                | 23.6 us: 1.11x faster                                                  |
| pickle_pure_python   | 304 us                                                 | 282 us: 1.08x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                   |
| pickle_list          | 4.17 us                                                | 4.04 us: 1.03x faster                                                  |
| pickle_dict          | 31.4 us                                                | 30.4 us: 1.03x faster                                                  |
| unpickle             | 13.3 us                                                | 12.9 us: 1.02x faster                                                  |
| xml_etree_process    | 53.8 ms                                                | 53.3 ms: 1.01x faster                                                  |
| unpickle_list        | 4.95 us                                                | 4.98 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.03x slower                                                   |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.58 ms: 1.03x slower                                                  |
| python_startup_no_site | 5.96 ms                                                | 6.13 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.0 ms: 1.11x faster                                                  |
| genshi_text     | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                  |
| mako            | 9.85 ms                                                | 9.77 ms: 1.01x faster                                                  |
| django_template | 32.5 ms                                                | 33.0 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.39 ms: 1.35x faster                                                  |
| deltablue               | 3.64 ms                                                | 3.20 ms: 1.14x faster                                                  |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                   |
| richards                | 46.2 ms                                                | 41.3 ms: 1.12x faster                                                  |
| json_loads              | 26.2 us                                                | 23.6 us: 1.11x faster                                                  |
| genshi_xml              | 52.1 ms                                                | 47.0 ms: 1.11x faster                                                  |
| logging_silent          | 98.5 ns                                                | 89.8 ns: 1.10x faster                                                  |
| genshi_text             | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                  |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| deepcopy_memo           | 36.4 us                                                | 33.8 us: 1.08x faster                                                  |
| pickle_pure_python      | 304 us                                                 | 282 us: 1.08x faster                                                   |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.11 ms: 1.07x faster                                                  |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                   |
| nqueens                 | 85.0 ms                                                | 80.3 ms: 1.06x faster                                                  |
| scimark_monte_carlo     | 68.3 ms                                                | 64.5 ms: 1.06x faster                                                  |
| html5lib                | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                  |
| logging_simple          | 6.06 us                                                | 5.74 us: 1.06x faster                                                  |
| coroutines              | 26.1 ms                                                | 24.7 ms: 1.06x faster                                                  |
| float                   | 76.3 ms                                                | 72.4 ms: 1.05x faster                                                  |
| hexiom                  | 6.35 ms                                                | 6.02 ms: 1.05x faster                                                  |
| scimark_fft             | 329 ms                                                 | 312 ms: 1.05x faster                                                   |
| json                    | 4.95 ms                                                | 4.70 ms: 1.05x faster                                                  |
| sqlglot_optimize        | 53.0 ms                                                | 50.3 ms: 1.05x faster                                                  |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                                   |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.05x faster                                                 |
| telco                   | 6.62 ms                                                | 6.33 ms: 1.05x faster                                                  |
| bench_thread_pool       | 810 us                                                 | 776 us: 1.04x faster                                                   |
| pyflate                 | 417 ms                                                 | 400 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| pprint_pformat          | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                 |
| deepcopy                | 344 us                                                 | 331 us: 1.04x faster                                                   |
| pickle_list             | 4.17 us                                                | 4.04 us: 1.03x faster                                                  |
| pickle_dict             | 31.4 us                                                | 30.4 us: 1.03x faster                                                  |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                 |
| sympy_integrate         | 20.9 ms                                                | 20.2 ms: 1.03x faster                                                  |
| logging_format          | 6.62 us                                                | 6.42 us: 1.03x faster                                                  |
| sympy_expand            | 472 ms                                                 | 458 ms: 1.03x faster                                                   |
| spectral_norm           | 99.9 ms                                                | 97.1 ms: 1.03x faster                                                  |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                   |
| chaos                   | 68.6 ms                                                | 66.8 ms: 1.03x faster                                                  |
| raytrace                | 290 ms                                                 | 283 ms: 1.03x faster                                                   |
| dulwich_log             | 63.9 ms                                                | 62.3 ms: 1.03x faster                                                  |
| pprint_safe_repr        | 691 ms                                                 | 673 ms: 1.03x faster                                                   |
| unpickle                | 13.3 us                                                | 12.9 us: 1.02x faster                                                  |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                                 |
| sympy_str               | 287 ms                                                 | 282 ms: 1.02x faster                                                   |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                   |
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                   |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.01x faster                                                  |
| async_generators        | 359 ms                                                 | 355 ms: 1.01x faster                                                   |
| xml_etree_process       | 53.8 ms                                                | 53.3 ms: 1.01x faster                                                  |
| mako                    | 9.85 ms                                                | 9.77 ms: 1.01x faster                                                  |
| deepcopy_reduce         | 2.97 us                                                | 2.95 us: 1.01x faster                                                  |
| thrift                  | 752 us                                                 | 755 us: 1.00x slower                                                   |
| unpickle_list           | 4.95 us                                                | 4.98 us: 1.01x slower                                                  |
| regex_v8                | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                  |
| scimark_lu              | 107 ms                                                 | 109 ms: 1.01x slower                                                   |
| crypto_pyaes            | 73.9 ms                                                | 74.8 ms: 1.01x slower                                                  |
| meteor_contest          | 105 ms                                                 | 106 ms: 1.01x slower                                                   |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                 |
| regex_dna               | 203 ms                                                 | 206 ms: 1.01x slower                                                   |
| sqlglot_parse           | 1.37 ms                                                | 1.39 ms: 1.02x slower                                                  |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                                  |
| django_template         | 32.5 ms                                                | 33.0 ms: 1.02x slower                                                  |
| python_startup          | 8.36 ms                                                | 8.58 ms: 1.03x slower                                                  |
| python_startup_no_site  | 5.96 ms                                                | 6.13 ms: 1.03x slower                                                  |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.03x slower                                                   |
| sqlite_synth            | 2.49 us                                                | 2.57 us: 1.03x slower                                                  |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                  |
| unpack_sequence         | 43.4 ns                                                | 45.1 ns: 1.04x slower                                                  |
| generators              | 72.2 ms                                                | 75.4 ms: 1.05x slower                                                  |
| async_tree_memoization  | 625 ms                                                 | 657 ms: 1.05x slower                                                   |
| regex_effbot            | 3.36 ms                                                | 3.61 ms: 1.07x slower                                                  |
| mypy                    | 669 ms                                                 | 810 ms: 1.21x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (7): nbody, chameleon, async_tree_none, bench_mp_pool, xml_etree_generate, async_tree_cpu_io_mixed, coverage
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230112-3.12.0a4+-d9dff4c/bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
