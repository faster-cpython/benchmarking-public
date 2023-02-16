
# Results vs. 3.11.0

- fork: penguin-wwy
- ref: add_return_none
- machine: linux-x86_64
- commit hash: f1deb5c
- commit date: 2023-02-07
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                     |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.05x faster                                                   |
| html5lib       | 64.8 ms                                                | 59.6 ms: 1.09x faster                                                    |
| tornado_http   | 96.5 ms                                                | 93.8 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.1 ms: 1.06x faster                                                    |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                                     |
| nbody          | 90.0 ms                                                | 95.5 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                     |
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                    |
| regex_dna      | 203 ms                                                 | 200 ms: 1.02x faster                                                     |
| regex_effbot   | 3.46 ms                                                | 3.50 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.37 ms: 1.32x faster                                                    |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                     |
| pickle_pure_python   | 308 us                                                 | 284 us: 1.09x faster                                                     |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                     |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                                    |
| pickle_list          | 4.14 us                                                | 4.07 us: 1.02x faster                                                    |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.02x faster                                                     |
| pickle               | 9.90 us                                                | 9.99 us: 1.01x slower                                                    |
| xml_etree_generate   | 75.9 ms                                                | 77.1 ms: 1.02x slower                                                    |
| unpickle_list        | 4.99 us                                                | 5.07 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.90 ms: 1.04x slower                                                    |
| python_startup_no_site | 6.04 ms                                                | 6.46 ms: 1.07x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.6 ms: 1.10x faster                                                    |
| genshi_text     | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                    |
| mako            | 9.83 ms                                                | 9.63 ms: 1.02x faster                                                    |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 491 ms: 1.80x faster                                                     |
| json_dumps              | 12.4 ms                                                | 9.37 ms: 1.32x faster                                                    |
| deltablue               | 3.66 ms                                                | 3.16 ms: 1.16x faster                                                    |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                     |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.01 ms: 1.14x faster                                                    |
| genshi_xml              | 51.4 ms                                                | 46.6 ms: 1.10x faster                                                    |
| richards                | 46.1 ms                                                | 41.9 ms: 1.10x faster                                                    |
| html5lib                | 64.8 ms                                                | 59.6 ms: 1.09x faster                                                    |
| gc_traversal            | 3.82 ms                                                | 3.52 ms: 1.09x faster                                                    |
| pickle_pure_python      | 308 us                                                 | 284 us: 1.09x faster                                                     |
| sympy_str               | 291 ms                                                 | 269 ms: 1.08x faster                                                     |
| logging_silent          | 98.0 ns                                                | 90.7 ns: 1.08x faster                                                    |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                     |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                     |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                                    |
| nqueens                 | 83.8 ms                                                | 77.8 ms: 1.08x faster                                                    |
| scimark_fft             | 325 ms                                                 | 303 ms: 1.07x faster                                                     |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                     |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                                   |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                     |
| float                   | 76.8 ms                                                | 72.1 ms: 1.06x faster                                                    |
| chaos                   | 68.7 ms                                                | 64.6 ms: 1.06x faster                                                    |
| hexiom                  | 6.34 ms                                                | 5.96 ms: 1.06x faster                                                    |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                    |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                   |
| logging_simple          | 6.02 us                                                | 5.69 us: 1.06x faster                                                    |
| pprint_safe_repr        | 706 ms                                                 | 668 ms: 1.06x faster                                                     |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                     |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                    |
| regex_v8                | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                    |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                     |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                    |
| bench_thread_pool       | 817 us                                                 | 780 us: 1.05x faster                                                     |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.05x faster                                                   |
| json                    | 4.87 ms                                                | 4.66 ms: 1.05x faster                                                    |
| scimark_monte_carlo     | 68.0 ms                                                | 65.3 ms: 1.04x faster                                                    |
| fannkuch                | 384 ms                                                 | 370 ms: 1.04x faster                                                     |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                                    |
| deepcopy_memo           | 35.8 us                                                | 34.5 us: 1.04x faster                                                    |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                     |
| coroutines              | 26.2 ms                                                | 25.3 ms: 1.03x faster                                                    |
| unpack_sequence         | 44.5 ns                                                | 43.0 ns: 1.03x faster                                                    |
| crypto_pyaes            | 75.7 ms                                                | 73.2 ms: 1.03x faster                                                    |
| spectral_norm           | 98.1 ms                                                | 94.9 ms: 1.03x faster                                                    |
| sqlglot_optimize        | 52.7 ms                                                | 51.0 ms: 1.03x faster                                                    |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.5 ms: 1.03x faster                                                    |
| pyflate                 | 419 ms                                                 | 406 ms: 1.03x faster                                                     |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                     |
| logging_format          | 6.48 us                                                | 6.29 us: 1.03x faster                                                    |
| tornado_http            | 96.5 ms                                                | 93.8 ms: 1.03x faster                                                    |
| deepcopy                | 341 us                                                 | 332 us: 1.03x faster                                                     |
| dulwich_log             | 64.0 ms                                                | 62.2 ms: 1.03x faster                                                    |
| thrift                  | 760 us                                                 | 739 us: 1.03x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                     |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                                    |
| raytrace                | 291 ms                                                 | 285 ms: 1.02x faster                                                     |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                    |
| mako                    | 9.83 ms                                                | 9.63 ms: 1.02x faster                                                    |
| async_generators        | 356 ms                                                 | 349 ms: 1.02x faster                                                     |
| pickle_list             | 4.14 us                                                | 4.07 us: 1.02x faster                                                    |
| regex_dna               | 203 ms                                                 | 200 ms: 1.02x faster                                                     |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                                     |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.02x faster                                                     |
| telco                   | 6.43 ms                                                | 6.33 ms: 1.01x faster                                                    |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                     |
| mdp                     | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                   |
| coverage                | 99.3 ms                                                | 98.4 ms: 1.01x faster                                                    |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                                     |
| pickle                  | 9.90 us                                                | 9.99 us: 1.01x slower                                                    |
| regex_effbot            | 3.46 ms                                                | 3.50 ms: 1.01x slower                                                    |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                                     |
| xml_etree_generate      | 75.9 ms                                                | 77.1 ms: 1.02x slower                                                    |
| unpickle_list           | 4.99 us                                                | 5.07 us: 1.02x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed | 736 ms                                                 | 754 ms: 1.02x slower                                                     |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                    |
| generators              | 73.5 ms                                                | 75.6 ms: 1.03x slower                                                    |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                    |
| python_startup          | 8.58 ms                                                | 8.90 ms: 1.04x slower                                                    |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                    |
| nbody                   | 90.0 ms                                                | 95.5 ms: 1.06x slower                                                    |
| async_tree_memoization  | 624 ms                                                 | 667 ms: 1.07x slower                                                     |
| python_startup_no_site  | 6.04 ms                                                | 6.46 ms: 1.07x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (6): unpickle, async_tree_none, xml_etree_process, djangocms, chameleon, bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, mypy2, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230207-3.12.0a4+-f1deb5c/bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c.json: mypy
