
# Results vs. 3.11.0

- fork: penguin-wwy
- ref: add_return_none
- machine: linux-x86_64
- commit hash: f1deb5c
- commit date: 2023-02-07
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 251 ms: 1.03x faster                                                     |
| chameleon      | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                    |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                   |
| html5lib       | 63.2 ms                                                | 59.6 ms: 1.06x faster                                                    |
| tornado_http   | 96.6 ms                                                | 93.8 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.1 ms: 1.06x faster                                                    |
| pidigits       | 199 ms                                                 | 197 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                     |
| regex_v8       | 22.3 ms                                                | 21.2 ms: 1.05x faster                                                    |
| regex_dna      | 203 ms                                                 | 200 ms: 1.02x faster                                                     |
| regex_effbot   | 3.36 ms                                                | 3.50 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.37 ms: 1.35x faster                                                    |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                     |
| json_loads           | 26.2 us                                                | 24.2 us: 1.08x faster                                                    |
| pickle_pure_python   | 304 us                                                 | 284 us: 1.07x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                     |
| pickle_dict          | 31.4 us                                                | 30.6 us: 1.03x faster                                                    |
| pickle_list          | 4.17 us                                                | 4.07 us: 1.03x faster                                                    |
| xml_etree_process    | 53.8 ms                                                | 53.5 ms: 1.00x faster                                                    |
| xml_etree_generate   | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                    |
| pickle               | 9.79 us                                                | 9.99 us: 1.02x slower                                                    |
| unpickle_list        | 4.95 us                                                | 5.07 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.90 ms: 1.06x slower                                                    |
| python_startup_no_site | 5.96 ms                                                | 6.46 ms: 1.08x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.6 ms: 1.12x faster                                                    |
| genshi_text     | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                    |
| mako            | 9.85 ms                                                | 9.63 ms: 1.02x faster                                                    |
| django_template | 32.5 ms                                                | 33.2 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.37 ms: 1.35x faster                                                    |
| deltablue               | 3.64 ms                                                | 3.16 ms: 1.15x faster                                                    |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                     |
| genshi_xml              | 52.1 ms                                                | 46.6 ms: 1.12x faster                                                    |
| richards                | 46.2 ms                                                | 41.9 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.01 ms: 1.10x faster                                                    |
| nqueens                 | 85.0 ms                                                | 77.8 ms: 1.09x faster                                                    |
| logging_silent          | 98.5 ns                                                | 90.7 ns: 1.09x faster                                                    |
| scimark_fft             | 329 ms                                                 | 303 ms: 1.09x faster                                                     |
| json_loads              | 26.2 us                                                | 24.2 us: 1.08x faster                                                    |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                     |
| genshi_text             | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                    |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                     |
| sympy_str               | 287 ms                                                 | 269 ms: 1.07x faster                                                     |
| pickle_pure_python      | 304 us                                                 | 284 us: 1.07x faster                                                     |
| logging_simple          | 6.06 us                                                | 5.69 us: 1.07x faster                                                    |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.07x faster                                                     |
| hexiom                  | 6.35 ms                                                | 5.96 ms: 1.07x faster                                                    |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                     |
| chaos                   | 68.6 ms                                                | 64.6 ms: 1.06x faster                                                    |
| json                    | 4.95 ms                                                | 4.66 ms: 1.06x faster                                                    |
| pycparser               | 1.17 sec                                               | 1.11 sec: 1.06x faster                                                   |
| html5lib                | 63.2 ms                                                | 59.6 ms: 1.06x faster                                                    |
| float                   | 76.3 ms                                                | 72.1 ms: 1.06x faster                                                    |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                                    |
| deepcopy_memo           | 36.4 us                                                | 34.5 us: 1.06x faster                                                    |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                    |
| spectral_norm           | 99.9 ms                                                | 94.9 ms: 1.05x faster                                                    |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                   |
| logging_format          | 6.62 us                                                | 6.29 us: 1.05x faster                                                    |
| go                      | 143 ms                                                 | 136 ms: 1.05x faster                                                     |
| regex_v8                | 22.3 ms                                                | 21.2 ms: 1.05x faster                                                    |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                     |
| fannkuch                | 388 ms                                                 | 370 ms: 1.05x faster                                                     |
| telco                   | 6.62 ms                                                | 6.33 ms: 1.05x faster                                                    |
| scimark_monte_carlo     | 68.3 ms                                                | 65.3 ms: 1.05x faster                                                    |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                   |
| sympy_expand            | 472 ms                                                 | 454 ms: 1.04x faster                                                     |
| bench_thread_pool       | 810 us                                                 | 780 us: 1.04x faster                                                     |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                                    |
| deepcopy                | 344 us                                                 | 332 us: 1.04x faster                                                     |
| pprint_safe_repr        | 691 ms                                                 | 668 ms: 1.03x faster                                                     |
| coroutines              | 26.1 ms                                                | 25.3 ms: 1.03x faster                                                    |
| tornado_http            | 96.6 ms                                                | 93.8 ms: 1.03x faster                                                    |
| async_generators        | 359 ms                                                 | 349 ms: 1.03x faster                                                     |
| dulwich_log             | 63.9 ms                                                | 62.2 ms: 1.03x faster                                                    |
| sqlalchemy_imperative   | 18.0 ms                                                | 17.5 ms: 1.03x faster                                                    |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                    |
| pickle_dict             | 31.4 us                                                | 30.6 us: 1.03x faster                                                    |
| 2to3                    | 257 ms                                                 | 251 ms: 1.03x faster                                                     |
| pyflate                 | 417 ms                                                 | 406 ms: 1.03x faster                                                     |
| pickle_list             | 4.17 us                                                | 4.07 us: 1.03x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                     |
| mako                    | 9.85 ms                                                | 9.63 ms: 1.02x faster                                                    |
| coverage                | 101 ms                                                 | 98.4 ms: 1.02x faster                                                    |
| raytrace                | 290 ms                                                 | 285 ms: 1.02x faster                                                     |
| regex_dna               | 203 ms                                                 | 200 ms: 1.02x faster                                                     |
| sqlalchemy_declarative  | 139 ms                                                 | 136 ms: 1.02x faster                                                     |
| thrift                  | 752 us                                                 | 739 us: 1.02x faster                                                     |
| scimark_lu              | 107 ms                                                 | 106 ms: 1.01x faster                                                     |
| pidigits                | 199 ms                                                 | 197 ms: 1.01x faster                                                     |
| async_tree_none         | 529 ms                                                 | 524 ms: 1.01x faster                                                     |
| crypto_pyaes            | 73.9 ms                                                | 73.2 ms: 1.01x faster                                                    |
| unpack_sequence         | 43.4 ns                                                | 43.0 ns: 1.01x faster                                                    |
| chameleon               | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                    |
| mdp                     | 2.62 sec                                               | 2.60 sec: 1.01x faster                                                   |
| deepcopy_reduce         | 2.97 us                                                | 2.95 us: 1.01x faster                                                    |
| xml_etree_process       | 53.8 ms                                                | 53.5 ms: 1.00x faster                                                    |
| xml_etree_generate      | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                    |
| meteor_contest          | 105 ms                                                 | 106 ms: 1.01x slower                                                     |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                                   |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                                    |
| pickle                  | 9.79 us                                                | 9.99 us: 1.02x slower                                                    |
| django_template         | 32.5 ms                                                | 33.2 ms: 1.02x slower                                                    |
| unpickle_list           | 4.95 us                                                | 5.07 us: 1.02x slower                                                    |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                                    |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                                    |
| regex_effbot            | 3.36 ms                                                | 3.50 ms: 1.04x slower                                                    |
| generators              | 72.2 ms                                                | 75.6 ms: 1.05x slower                                                    |
| python_startup          | 8.36 ms                                                | 8.90 ms: 1.06x slower                                                    |
| async_tree_memoization  | 625 ms                                                 | 667 ms: 1.07x slower                                                     |
| python_startup_no_site  | 5.96 ms                                                | 6.46 ms: 1.08x slower                                                    |
| mypy                    | 669 ms                                                 | 803 ms: 1.20x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (5): unpickle, xml_etree_iterparse, bench_mp_pool, async_tree_cpu_io_mixed, nbody
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20230207-3.12.0a4+-f1deb5c/bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal
