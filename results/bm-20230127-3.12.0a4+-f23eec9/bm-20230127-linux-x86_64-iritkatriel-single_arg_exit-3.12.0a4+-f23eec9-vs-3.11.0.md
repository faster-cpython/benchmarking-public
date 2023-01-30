
# Results vs. 3.11.0

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: f23eec9
- commit date: 2023-01-27
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 251 ms: 1.02x faster                                                   |
| chameleon      | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                  |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                 |
| html5lib       | 63.2 ms                                                | 60.2 ms: 1.05x faster                                                  |
| tornado_http   | 96.6 ms                                                | 93.9 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.7 ms: 1.06x faster                                                  |
| nbody          | 95.0 ms                                                | 94.0 ms: 1.01x faster                                                  |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                                   |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                   |
| regex_effbot   | 3.36 ms                                                | 3.57 ms: 1.07x slower                                                  |
| regex_v8       | 22.3 ms                                                | 26.0 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.38 ms: 1.35x faster                                                  |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                   |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| pickle_pure_python   | 304 us                                                 | 282 us: 1.08x faster                                                   |
| pickle_list          | 4.17 us                                                | 4.03 us: 1.04x faster                                                  |
| pickle_dict          | 31.4 us                                                | 30.8 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.00x faster                                                   |
| xml_etree_generate   | 76.2 ms                                                | 77.3 ms: 1.01x slower                                                  |
| unpickle_list        | 4.95 us                                                | 5.04 us: 1.02x slower                                                  |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.90 ms: 1.07x slower                                                  |
| python_startup_no_site | 5.96 ms                                                | 6.45 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.5 ms: 1.12x faster                                                  |
| genshi_text     | 22.1 ms                                                | 20.7 ms: 1.07x faster                                                  |
| mako            | 9.85 ms                                                | 9.71 ms: 1.01x faster                                                  |
| django_template | 32.5 ms                                                | 32.8 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.38 ms: 1.35x faster                                                  |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                   |
| deltablue               | 3.64 ms                                                | 3.21 ms: 1.14x faster                                                  |
| genshi_xml              | 52.1 ms                                                | 46.5 ms: 1.12x faster                                                  |
| nqueens                 | 85.0 ms                                                | 76.3 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.02 ms: 1.10x faster                                                  |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                                  |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| richards                | 46.2 ms                                                | 42.5 ms: 1.09x faster                                                  |
| scimark_fft             | 329 ms                                                 | 303 ms: 1.09x faster                                                   |
| json                    | 4.95 ms                                                | 4.56 ms: 1.09x faster                                                  |
| logging_simple          | 6.06 us                                                | 5.62 us: 1.08x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| pickle_pure_python      | 304 us                                                 | 282 us: 1.08x faster                                                   |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                   |
| logging_format          | 6.62 us                                                | 6.19 us: 1.07x faster                                                  |
| genshi_text             | 22.1 ms                                                | 20.7 ms: 1.07x faster                                                  |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                   |
| sympy_str               | 287 ms                                                 | 270 ms: 1.07x faster                                                   |
| coroutines              | 26.1 ms                                                | 24.5 ms: 1.07x faster                                                  |
| float                   | 76.3 ms                                                | 71.7 ms: 1.06x faster                                                  |
| chaos                   | 68.6 ms                                                | 64.9 ms: 1.06x faster                                                  |
| hexiom                  | 6.35 ms                                                | 6.00 ms: 1.06x faster                                                  |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                                  |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.05x faster                                                  |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                                   |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                   |
| html5lib                | 63.2 ms                                                | 60.2 ms: 1.05x faster                                                  |
| deepcopy_memo           | 36.4 us                                                | 34.8 us: 1.05x faster                                                  |
| go                      | 143 ms                                                 | 137 ms: 1.05x faster                                                   |
| pyflate                 | 417 ms                                                 | 399 ms: 1.04x faster                                                   |
| bench_thread_pool       | 810 us                                                 | 776 us: 1.04x faster                                                   |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                                   |
| pprint_pformat          | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                 |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                 |
| logging_silent          | 98.5 ns                                                | 94.9 ns: 1.04x faster                                                  |
| scimark_monte_carlo     | 68.3 ms                                                | 65.8 ms: 1.04x faster                                                  |
| telco                   | 6.62 ms                                                | 6.39 ms: 1.04x faster                                                  |
| pickle_list             | 4.17 us                                                | 4.03 us: 1.04x faster                                                  |
| coverage                | 101 ms                                                 | 97.2 ms: 1.03x faster                                                  |
| sqlglot_optimize        | 53.0 ms                                                | 51.3 ms: 1.03x faster                                                  |
| deepcopy                | 344 us                                                 | 334 us: 1.03x faster                                                   |
| raytrace                | 290 ms                                                 | 282 ms: 1.03x faster                                                   |
| pycparser               | 1.17 sec                                               | 1.14 sec: 1.03x faster                                                 |
| tornado_http            | 96.6 ms                                                | 93.9 ms: 1.03x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                  |
| 2to3                    | 257 ms                                                 | 251 ms: 1.02x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                 |
| dulwich_log             | 63.9 ms                                                | 62.6 ms: 1.02x faster                                                  |
| async_generators        | 359 ms                                                 | 352 ms: 1.02x faster                                                   |
| chameleon               | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                  |
| pprint_safe_repr        | 691 ms                                                 | 678 ms: 1.02x faster                                                   |
| pickle_dict             | 31.4 us                                                | 30.8 us: 1.02x faster                                                  |
| mako                    | 9.85 ms                                                | 9.71 ms: 1.01x faster                                                  |
| crypto_pyaes            | 73.9 ms                                                | 73.0 ms: 1.01x faster                                                  |
| nbody                   | 95.0 ms                                                | 94.0 ms: 1.01x faster                                                  |
| async_tree_none         | 529 ms                                                 | 524 ms: 1.01x faster                                                   |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                                   |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                   |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.00x faster                                                   |
| async_tree_cpu_io_mixed | 752 ms                                                 | 758 ms: 1.01x slower                                                   |
| django_template         | 32.5 ms                                                | 32.8 ms: 1.01x slower                                                  |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                 |
| unpack_sequence         | 43.4 ns                                                | 44.0 ns: 1.01x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 77.3 ms: 1.01x slower                                                  |
| unpickle_list           | 4.95 us                                                | 5.04 us: 1.02x slower                                                  |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.03x slower                                                  |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                  |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                   |
| async_tree_memoization  | 625 ms                                                 | 645 ms: 1.03x slower                                                   |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                                  |
| regex_effbot            | 3.36 ms                                                | 3.57 ms: 1.07x slower                                                  |
| python_startup          | 8.36 ms                                                | 8.90 ms: 1.07x slower                                                  |
| generators              | 72.2 ms                                                | 77.4 ms: 1.07x slower                                                  |
| python_startup_no_site  | 5.96 ms                                                | 6.45 ms: 1.08x slower                                                  |
| regex_v8                | 22.3 ms                                                | 26.0 ms: 1.17x slower                                                  |
| mypy                    | 669 ms                                                 | 806 ms: 1.21x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (7): unpickle, thrift, xml_etree_process, scimark_lu, bench_mp_pool, spectral_norm, deepcopy_reduce
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230127-3.12.0a4+-f23eec9/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
