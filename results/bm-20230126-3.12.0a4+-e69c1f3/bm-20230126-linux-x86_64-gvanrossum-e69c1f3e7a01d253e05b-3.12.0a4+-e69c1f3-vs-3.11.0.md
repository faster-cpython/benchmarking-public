
# Results vs. 3.11.0

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: linux-x86_64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 250 ms: 1.03x faster                                                       |
| chameleon      | 6.41 ms                                                | 6.38 ms: 1.00x faster                                                      |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| html5lib       | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                      |
| tornado_http   | 96.6 ms                                                | 94.1 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.8 ms: 1.06x faster                                                      |
| pidigits       | 199 ms                                                 | 193 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                       |
| regex_v8       | 22.3 ms                                                | 21.2 ms: 1.05x faster                                                      |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                       |
| regex_effbot   | 3.36 ms                                                | 3.54 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.40 ms: 1.35x faster                                                      |
| unpickle_pure_python | 225 us                                                 | 196 us: 1.15x faster                                                       |
| json_loads           | 26.2 us                                                | 24.0 us: 1.10x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.07x faster                                                       |
| pickle_pure_python   | 304 us                                                 | 286 us: 1.06x faster                                                       |
| pickle_list          | 4.17 us                                                | 3.96 us: 1.05x faster                                                      |
| pickle_dict          | 31.4 us                                                | 30.4 us: 1.03x faster                                                      |
| unpickle_list        | 4.95 us                                                | 5.01 us: 1.01x slower                                                      |
| pickle               | 9.79 us                                                | 10.0 us: 1.02x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 78.3 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (3): unpickle, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.90 ms: 1.07x slower                                                      |
| python_startup_no_site | 5.96 ms                                                | 6.44 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 47.3 ms: 1.10x faster                                                      |
| genshi_text    | 22.1 ms                                                | 21.2 ms: 1.04x faster                                                      |
| mako           | 9.85 ms                                                | 9.70 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.40 ms: 1.35x faster                                                      |
| unpickle_pure_python    | 225 us                                                 | 196 us: 1.15x faster                                                       |
| deltablue               | 3.64 ms                                                | 3.22 ms: 1.13x faster                                                      |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.95 ms: 1.11x faster                                                      |
| richards                | 46.2 ms                                                | 41.7 ms: 1.11x faster                                                      |
| genshi_xml              | 52.1 ms                                                | 47.3 ms: 1.10x faster                                                      |
| json_loads              | 26.2 us                                                | 24.0 us: 1.10x faster                                                      |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                       |
| nqueens                 | 85.0 ms                                                | 78.5 ms: 1.08x faster                                                      |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.07x faster                                                       |
| chaos                   | 68.6 ms                                                | 64.0 ms: 1.07x faster                                                      |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                       |
| json                    | 4.95 ms                                                | 4.63 ms: 1.07x faster                                                      |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                       |
| scimark_fft             | 329 ms                                                 | 308 ms: 1.07x faster                                                       |
| sympy_str               | 287 ms                                                 | 269 ms: 1.07x faster                                                       |
| pycparser               | 1.17 sec                                               | 1.10 sec: 1.07x faster                                                     |
| logging_silent          | 98.5 ns                                                | 92.5 ns: 1.06x faster                                                      |
| float                   | 76.3 ms                                                | 71.8 ms: 1.06x faster                                                      |
| logging_simple          | 6.06 us                                                | 5.71 us: 1.06x faster                                                      |
| deepcopy_memo           | 36.4 us                                                | 34.3 us: 1.06x faster                                                      |
| pickle_pure_python      | 304 us                                                 | 286 us: 1.06x faster                                                       |
| hexiom                  | 6.35 ms                                                | 5.99 ms: 1.06x faster                                                      |
| fannkuch                | 388 ms                                                 | 367 ms: 1.06x faster                                                       |
| html5lib                | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                      |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                                      |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.06x faster                                                     |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.05x faster                                                      |
| pickle_list             | 4.17 us                                                | 3.96 us: 1.05x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 993 us: 1.05x faster                                                       |
| telco                   | 6.62 ms                                                | 6.30 ms: 1.05x faster                                                      |
| go                      | 143 ms                                                 | 136 ms: 1.05x faster                                                       |
| regex_v8                | 22.3 ms                                                | 21.2 ms: 1.05x faster                                                      |
| deepcopy                | 344 us                                                 | 327 us: 1.05x faster                                                       |
| logging_format          | 6.62 us                                                | 6.31 us: 1.05x faster                                                      |
| scimark_monte_carlo     | 68.3 ms                                                | 65.2 ms: 1.05x faster                                                      |
| coverage                | 101 ms                                                 | 96.1 ms: 1.05x faster                                                      |
| pyflate                 | 417 ms                                                 | 399 ms: 1.05x faster                                                       |
| sympy_expand            | 472 ms                                                 | 451 ms: 1.05x faster                                                       |
| genshi_text             | 22.1 ms                                                | 21.2 ms: 1.04x faster                                                      |
| sqlglot_optimize        | 53.0 ms                                                | 50.7 ms: 1.04x faster                                                      |
| bench_thread_pool       | 810 us                                                 | 779 us: 1.04x faster                                                       |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                       |
| pidigits                | 199 ms                                                 | 193 ms: 1.04x faster                                                       |
| pprint_safe_repr        | 691 ms                                                 | 667 ms: 1.04x faster                                                       |
| unpack_sequence         | 43.4 ns                                                | 41.9 ns: 1.03x faster                                                      |
| coroutines              | 26.1 ms                                                | 25.2 ms: 1.03x faster                                                      |
| pickle_dict             | 31.4 us                                                | 30.4 us: 1.03x faster                                                      |
| 2to3                    | 257 ms                                                 | 250 ms: 1.03x faster                                                       |
| dulwich_log             | 63.9 ms                                                | 62.1 ms: 1.03x faster                                                      |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.03x faster                                                     |
| tornado_http            | 96.6 ms                                                | 94.1 ms: 1.03x faster                                                      |
| crypto_pyaes            | 73.9 ms                                                | 72.1 ms: 1.03x faster                                                      |
| async_generators        | 359 ms                                                 | 351 ms: 1.02x faster                                                       |
| raytrace                | 290 ms                                                 | 284 ms: 1.02x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                      |
| mako                    | 9.85 ms                                                | 9.70 ms: 1.01x faster                                                      |
| async_tree_none         | 529 ms                                                 | 523 ms: 1.01x faster                                                       |
| thrift                  | 752 us                                                 | 746 us: 1.01x faster                                                       |
| chameleon               | 6.41 ms                                                | 6.38 ms: 1.00x faster                                                      |
| unpickle_list           | 4.95 us                                                | 5.01 us: 1.01x slower                                                      |
| deepcopy_reduce         | 2.97 us                                                | 3.00 us: 1.01x slower                                                      |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                       |
| pickle                  | 9.79 us                                                | 10.0 us: 1.02x slower                                                      |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.03x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 78.3 ms: 1.03x slower                                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.42 ms: 1.04x slower                                                      |
| generators              | 72.2 ms                                                | 75.1 ms: 1.04x slower                                                      |
| sqlite_synth            | 2.49 us                                                | 2.61 us: 1.05x slower                                                      |
| regex_effbot            | 3.36 ms                                                | 3.54 ms: 1.06x slower                                                      |
| python_startup          | 8.36 ms                                                | 8.90 ms: 1.07x slower                                                      |
| python_startup_no_site  | 5.96 ms                                                | 6.44 ms: 1.08x slower                                                      |
| mypy                    | 669 ms                                                 | 806 ms: 1.20x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (12): unpickle, spectral_norm, async_tree_io, bench_mp_pool, meteor_contest, async_tree_memoization, django_template, nbody, xml_etree_process, async_tree_cpu_io_mixed, xml_etree_iterparse, scimark_lu
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
