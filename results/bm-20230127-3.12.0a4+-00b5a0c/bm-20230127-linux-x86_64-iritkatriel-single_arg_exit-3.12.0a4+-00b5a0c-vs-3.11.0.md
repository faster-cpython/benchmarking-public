
# Results vs. 3.11.0

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: 00b5a0c
- commit date: 2023-01-27
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 254 ms: 1.01x faster                                                   |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                 |
| html5lib       | 63.2 ms                                                | 60.6 ms: 1.04x faster                                                  |
| tornado_http   | 96.6 ms                                                | 94.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.5 ms: 1.05x faster                                                  |
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                   |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                                   |
| regex_effbot   | 3.36 ms                                                | 3.37 ms: 1.01x slower                                                  |
| regex_v8       | 22.3 ms                                                | 21.5 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.32 ms: 1.36x faster                                                  |
| json_loads           | 26.2 us                                                | 25.7 us: 1.02x faster                                                  |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                                  |
| pickle_dict          | 31.4 us                                                | 31.3 us: 1.00x faster                                                  |
| pickle_list          | 4.17 us                                                | 4.15 us: 1.01x faster                                                  |
| pickle_pure_python   | 304 us                                                 | 285 us: 1.07x faster                                                   |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                                  |
| unpickle_pure_python | 225 us                                                 | 201 us: 1.12x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 146 ms: 1.08x faster                                                   |
| xml_etree_generate   | 76.2 ms                                                | 77.8 ms: 1.02x slower                                                  |
| xml_etree_process    | 53.8 ms                                                | 53.5 ms: 1.00x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.96 ms: 1.07x slower                                                  |
| python_startup_no_site | 5.96 ms                                                | 6.54 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 33.3 ms: 1.03x slower                                                  |
| genshi_text     | 22.1 ms                                                | 20.4 ms: 1.08x faster                                                  |
| genshi_xml      | 52.1 ms                                                | 46.7 ms: 1.11x faster                                                  |
| mako            | 9.85 ms                                                | 9.45 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 254 ms: 1.01x faster                                                   |
| aiohttp                 | 1.05 ms                                                | 1.02 ms: 1.03x faster                                                  |
| async_generators        | 359 ms                                                 | 352 ms: 1.02x faster                                                   |
| async_tree_none         | 529 ms                                                 | 517 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed | 752 ms                                                 | 747 ms: 1.01x faster                                                   |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                 |
| async_tree_memoization  | 625 ms                                                 | 646 ms: 1.03x slower                                                   |
| chaos                   | 68.6 ms                                                | 67.2 ms: 1.02x faster                                                  |
| bench_mp_pool           | 24.0 ms                                                | 30.6 ms: 1.27x slower                                                  |
| bench_thread_pool       | 810 us                                                 | 963 us: 1.19x slower                                                   |
| coroutines              | 26.1 ms                                                | 25.2 ms: 1.04x faster                                                  |
| coverage                | 101 ms                                                 | 99.4 ms: 1.01x faster                                                  |
| crypto_pyaes            | 73.9 ms                                                | 73.1 ms: 1.01x faster                                                  |
| deepcopy                | 344 us                                                 | 330 us: 1.04x faster                                                   |
| deepcopy_reduce         | 2.97 us                                                | 2.92 us: 1.02x faster                                                  |
| deepcopy_memo           | 36.4 us                                                | 33.8 us: 1.08x faster                                                  |
| deltablue               | 3.64 ms                                                | 3.25 ms: 1.12x faster                                                  |
| django_template         | 32.5 ms                                                | 33.3 ms: 1.03x slower                                                  |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                 |
| dulwich_log             | 63.9 ms                                                | 62.7 ms: 1.02x faster                                                  |
| fannkuch                | 388 ms                                                 | 381 ms: 1.02x faster                                                   |
| float                   | 76.3 ms                                                | 72.5 ms: 1.05x faster                                                  |
| generators              | 72.2 ms                                                | 78.4 ms: 1.09x slower                                                  |
| genshi_text             | 22.1 ms                                                | 20.4 ms: 1.08x faster                                                  |
| genshi_xml              | 52.1 ms                                                | 46.7 ms: 1.11x faster                                                  |
| go                      | 143 ms                                                 | 138 ms: 1.04x faster                                                   |
| gunicorn                | 1.12 ms                                                | 1.10 ms: 1.02x faster                                                  |
| hexiom                  | 6.35 ms                                                | 5.98 ms: 1.06x faster                                                  |
| html5lib                | 63.2 ms                                                | 60.6 ms: 1.04x faster                                                  |
| json                    | 4.95 ms                                                | 4.78 ms: 1.04x faster                                                  |
| json_dumps              | 12.7 ms                                                | 9.32 ms: 1.36x faster                                                  |
| json_loads              | 26.2 us                                                | 25.7 us: 1.02x faster                                                  |
| logging_format          | 6.62 us                                                | 6.45 us: 1.03x faster                                                  |
| logging_silent          | 98.5 ns                                                | 92.0 ns: 1.07x faster                                                  |
| logging_simple          | 6.06 us                                                | 5.87 us: 1.03x faster                                                  |
| mako                    | 9.85 ms                                                | 9.45 ms: 1.04x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.47 sec: 1.06x faster                                                 |
| mypy                    | 669 ms                                                 | 647 ms: 1.03x faster                                                   |
| nqueens                 | 85.0 ms                                                | 76.3 ms: 1.11x faster                                                  |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                  |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                                  |
| pickle_dict             | 31.4 us                                                | 31.3 us: 1.00x faster                                                  |
| pickle_list             | 4.17 us                                                | 4.15 us: 1.01x faster                                                  |
| pickle_pure_python      | 304 us                                                 | 285 us: 1.07x faster                                                   |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                                   |
| pprint_safe_repr        | 691 ms                                                 | 671 ms: 1.03x faster                                                   |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.05x faster                                                 |
| pycparser               | 1.17 sec                                               | 1.12 sec: 1.04x faster                                                 |
| pyflate                 | 417 ms                                                 | 394 ms: 1.06x faster                                                   |
| python_startup          | 8.36 ms                                                | 8.96 ms: 1.07x slower                                                  |
| python_startup_no_site  | 5.96 ms                                                | 6.54 ms: 1.10x slower                                                  |
| raytrace                | 290 ms                                                 | 283 ms: 1.03x faster                                                   |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                   |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                                   |
| regex_effbot            | 3.36 ms                                                | 3.37 ms: 1.01x slower                                                  |
| regex_v8                | 22.3 ms                                                | 21.5 ms: 1.04x faster                                                  |
| richards                | 46.2 ms                                                | 42.4 ms: 1.09x faster                                                  |
| scimark_fft             | 329 ms                                                 | 311 ms: 1.06x faster                                                   |
| scimark_lu              | 107 ms                                                 | 112 ms: 1.04x slower                                                   |
| scimark_monte_carlo     | 68.3 ms                                                | 67.1 ms: 1.02x faster                                                  |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.17 ms: 1.06x faster                                                  |
| spectral_norm           | 99.9 ms                                                | 95.4 ms: 1.05x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                  |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 53.0 ms                                                | 52.1 ms: 1.02x faster                                                  |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                                  |
| sympy_expand            | 472 ms                                                 | 461 ms: 1.02x faster                                                   |
| sympy_integrate         | 20.9 ms                                                | 20.0 ms: 1.05x faster                                                  |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.07x faster                                                   |
| sympy_str               | 287 ms                                                 | 273 ms: 1.05x faster                                                   |
| telco                   | 6.62 ms                                                | 6.25 ms: 1.06x faster                                                  |
| tornado_http            | 96.6 ms                                                | 94.7 ms: 1.02x faster                                                  |
| unpack_sequence         | 43.4 ns                                                | 43.8 ns: 1.01x slower                                                  |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                                  |
| unpickle_pure_python    | 225 us                                                 | 201 us: 1.12x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 146 ms: 1.08x faster                                                   |
| xml_etree_generate      | 76.2 ms                                                | 77.8 ms: 1.02x slower                                                  |
| xml_etree_process       | 53.8 ms                                                | 53.5 ms: 1.00x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (7): chameleon, meteor_contest, nbody, sqlglot_normalize, thrift, unpickle_list, xml_etree_iterparse
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230127-3.12.0a4+-00b5a0c/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
