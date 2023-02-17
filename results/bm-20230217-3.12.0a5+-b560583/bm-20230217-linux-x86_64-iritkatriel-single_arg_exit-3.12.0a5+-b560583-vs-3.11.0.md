
# Results vs. 3.11.0

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: b560583
- commit date: 2023-02-17
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.05x faster                                                   |
| chameleon      | 6.38 ms                                                | 6.29 ms: 1.01x faster                                                  |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                 |
| html5lib       | 64.8 ms                                                | 61.7 ms: 1.05x faster                                                  |
| tornado_http   | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                  |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                   |
| nbody          | 90.0 ms                                                | 93.1 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                   |
| regex_effbot   | 3.46 ms                                                | 3.28 ms: 1.05x faster                                                  |
| regex_v8       | 22.2 ms                                                | 21.3 ms: 1.04x faster                                                  |
| regex_dna      | 203 ms                                                 | 212 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.33 ms: 1.32x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 196 us: 1.16x faster                                                   |
| json_loads           | 26.1 us                                                | 23.5 us: 1.11x faster                                                  |
| pickle_pure_python   | 308 us                                                 | 281 us: 1.10x faster                                                   |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                   |
| pickle_dict          | 31.2 us                                                | 31.4 us: 1.01x slower                                                  |
| pickle_list          | 4.14 us                                                | 4.18 us: 1.01x slower                                                  |
| unpickle_list        | 4.99 us                                                | 5.08 us: 1.02x slower                                                  |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                  |
| xml_etree_process    | 53.7 ms                                                | 56.2 ms: 1.05x slower                                                  |
| xml_etree_generate   | 75.9 ms                                                | 80.7 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.97 ms: 1.05x slower                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.50 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.0 ms: 1.07x faster                                                  |
| genshi_text     | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                  |
| mako            | 9.83 ms                                                | 9.89 ms: 1.01x slower                                                  |
| django_template | 32.3 ms                                                | 33.6 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.3 ms: 2.35x faster                                                  |
| asyncio_tcp             | 883 ms                                                 | 501 ms: 1.76x faster                                                   |
| json_dumps              | 12.4 ms                                                | 9.33 ms: 1.32x faster                                                  |
| mypy2                   | 420 ms                                                 | 329 ms: 1.28x faster                                                   |
| unpickle_pure_python    | 227 us                                                 | 196 us: 1.16x faster                                                   |
| coroutines              | 26.2 ms                                                | 22.7 ms: 1.15x faster                                                  |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.08 ms: 1.13x faster                                                  |
| json_loads              | 26.1 us                                                | 23.5 us: 1.11x faster                                                  |
| pickle_pure_python      | 308 us                                                 | 281 us: 1.10x faster                                                   |
| richards                | 46.1 ms                                                | 42.4 ms: 1.09x faster                                                  |
| gc_traversal            | 3.82 ms                                                | 3.53 ms: 1.08x faster                                                  |
| nqueens                 | 83.8 ms                                                | 77.6 ms: 1.08x faster                                                  |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                   |
| unpack_sequence         | 44.5 ns                                                | 41.3 ns: 1.08x faster                                                  |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                 |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                   |
| genshi_xml              | 51.4 ms                                                | 48.0 ms: 1.07x faster                                                  |
| sympy_str               | 291 ms                                                 | 272 ms: 1.07x faster                                                   |
| json                    | 4.87 ms                                                | 4.55 ms: 1.07x faster                                                  |
| scimark_fft             | 325 ms                                                 | 306 ms: 1.06x faster                                                   |
| logging_silent          | 98.0 ns                                                | 92.1 ns: 1.06x faster                                                  |
| float                   | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                  |
| spectral_norm           | 98.1 ms                                                | 92.9 ms: 1.06x faster                                                  |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                   |
| regex_effbot            | 3.46 ms                                                | 3.28 ms: 1.05x faster                                                  |
| pprint_safe_repr        | 706 ms                                                 | 670 ms: 1.05x faster                                                   |
| 2to3                    | 259 ms                                                 | 246 ms: 1.05x faster                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                 |
| logging_simple          | 6.02 us                                                | 5.73 us: 1.05x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 19.9 ms: 1.05x faster                                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 64.7 ms: 1.05x faster                                                  |
| html5lib                | 64.8 ms                                                | 61.7 ms: 1.05x faster                                                  |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                                   |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                  |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                                   |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                   |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.05x faster                                                   |
| deepcopy_memo           | 35.8 us                                                | 34.3 us: 1.04x faster                                                  |
| crypto_pyaes            | 75.7 ms                                                | 72.6 ms: 1.04x faster                                                  |
| regex_v8                | 22.2 ms                                                | 21.3 ms: 1.04x faster                                                  |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                   |
| bench_thread_pool       | 817 us                                                 | 785 us: 1.04x faster                                                   |
| hexiom                  | 6.34 ms                                                | 6.10 ms: 1.04x faster                                                  |
| sqlglot_optimize        | 52.7 ms                                                | 50.8 ms: 1.04x faster                                                  |
| chaos                   | 68.7 ms                                                | 66.2 ms: 1.04x faster                                                  |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                   |
| coverage                | 99.3 ms                                                | 96.4 ms: 1.03x faster                                                  |
| deepcopy_reduce         | 3.02 us                                                | 2.93 us: 1.03x faster                                                  |
| genshi_text             | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                  |
| pyflate                 | 419 ms                                                 | 408 ms: 1.03x faster                                                   |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                 |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                                  |
| telco                   | 6.43 ms                                                | 6.29 ms: 1.02x faster                                                  |
| dulwich_log             | 64.0 ms                                                | 62.6 ms: 1.02x faster                                                  |
| deepcopy                | 341 us                                                 | 335 us: 1.02x faster                                                   |
| tornado_http            | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                   |
| chameleon               | 6.38 ms                                                | 6.29 ms: 1.01x faster                                                  |
| mdp                     | 2.63 sec                                               | 2.62 sec: 1.00x faster                                                 |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                  |
| mako                    | 9.83 ms                                                | 9.89 ms: 1.01x slower                                                  |
| pickle_dict             | 31.2 us                                                | 31.4 us: 1.01x slower                                                  |
| pickle_list             | 4.14 us                                                | 4.18 us: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 745 ms: 1.01x slower                                                   |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| pathlib                 | 18.1 ms                                                | 18.4 ms: 1.02x slower                                                  |
| unpickle_list           | 4.99 us                                                | 5.08 us: 1.02x slower                                                  |
| nbody                   | 90.0 ms                                                | 93.1 ms: 1.03x slower                                                  |
| django_template         | 32.3 ms                                                | 33.6 ms: 1.04x slower                                                  |
| regex_dna               | 203 ms                                                 | 212 ms: 1.04x slower                                                   |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                                  |
| python_startup          | 8.58 ms                                                | 8.97 ms: 1.05x slower                                                  |
| xml_etree_process       | 53.7 ms                                                | 56.2 ms: 1.05x slower                                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.63 us: 1.06x slower                                                  |
| async_tree_memoization  | 624 ms                                                 | 663 ms: 1.06x slower                                                   |
| xml_etree_generate      | 75.9 ms                                                | 80.7 ms: 1.06x slower                                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.50 ms: 1.08x slower                                                  |
| async_generators        | 356 ms                                                 | 412 ms: 1.16x slower                                                   |
| dask                    | 365 ms                                                 | 499 ms: 1.37x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (7): unpickle, meteor_contest, sqlalchemy_imperative, thrift, djangocms, scimark_lu, async_tree_none
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
