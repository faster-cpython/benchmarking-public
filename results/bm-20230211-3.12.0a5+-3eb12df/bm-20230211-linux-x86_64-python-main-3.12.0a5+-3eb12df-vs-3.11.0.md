
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3eb12df
- commit date: 2023-02-11
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                   |
| chameleon      | 6.38 ms                                                | 6.58 ms: 1.03x slower                                  |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                 |
| html5lib       | 64.8 ms                                                | 61.1 ms: 1.06x faster                                  |
| tornado_http   | 96.5 ms                                                | 94.5 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.1 ms: 1.07x faster                                  |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                   |
| nbody          | 90.0 ms                                                | 94.8 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                   |
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                  |
| regex_dna      | 203 ms                                                 | 199 ms: 1.02x faster                                   |
| regex_effbot   | 3.46 ms                                                | 3.56 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.51 ms: 1.30x faster                                  |
| unpickle_pure_python | 227 us                                                 | 196 us: 1.16x faster                                   |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                   |
| pickle_pure_python   | 308 us                                                 | 288 us: 1.07x faster                                   |
| pickle_list          | 4.14 us                                                | 4.05 us: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_dict          | 31.2 us                                                | 30.8 us: 1.01x faster                                  |
| unpickle_list        | 4.99 us                                                | 4.95 us: 1.01x faster                                  |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                  |
| xml_etree_process    | 53.7 ms                                                | 55.2 ms: 1.03x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 80.5 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.92 ms: 1.04x slower                                  |
| python_startup_no_site | 6.04 ms                                                | 6.47 ms: 1.07x slower                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.6 ms: 1.10x faster                                  |
| genshi_text     | 21.5 ms                                                | 20.6 ms: 1.05x faster                                  |
| mako            | 9.83 ms                                                | 9.95 ms: 1.01x slower                                  |
| django_template | 32.3 ms                                                | 33.3 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 498 ms: 1.77x faster                                   |
| json_dumps              | 12.4 ms                                                | 9.51 ms: 1.30x faster                                  |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                   |
| deltablue               | 3.66 ms                                                | 3.11 ms: 1.17x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 196 us: 1.16x faster                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.13 ms: 1.11x faster                                  |
| genshi_xml              | 51.4 ms                                                | 46.6 ms: 1.10x faster                                  |
| richards                | 46.1 ms                                                | 42.3 ms: 1.09x faster                                  |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                  |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                 |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                   |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                   |
| nqueens                 | 83.8 ms                                                | 77.6 ms: 1.08x faster                                  |
| logging_silent          | 98.0 ns                                                | 91.0 ns: 1.08x faster                                  |
| hexiom                  | 6.34 ms                                                | 5.91 ms: 1.07x faster                                  |
| pickle_pure_python      | 308 us                                                 | 288 us: 1.07x faster                                   |
| sympy_str               | 291 ms                                                 | 273 ms: 1.07x faster                                   |
| float                   | 76.8 ms                                                | 72.1 ms: 1.07x faster                                  |
| mdp                     | 2.63 sec                                               | 2.47 sec: 1.06x faster                                 |
| html5lib                | 64.8 ms                                                | 61.1 ms: 1.06x faster                                  |
| fannkuch                | 384 ms                                                 | 363 ms: 1.06x faster                                   |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 19.9 ms: 1.06x faster                                  |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                   |
| pyflate                 | 419 ms                                                 | 398 ms: 1.05x faster                                   |
| json                    | 4.87 ms                                                | 4.63 ms: 1.05x faster                                  |
| regex_v8                | 22.2 ms                                                | 21.2 ms: 1.05x faster                                  |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.05x faster                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.45 ms: 1.05x faster                                  |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                   |
| deepcopy_memo           | 35.8 us                                                | 34.3 us: 1.04x faster                                  |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                  |
| sympy_sum               | 166 ms                                                 | 159 ms: 1.04x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                 |
| bench_thread_pool       | 817 us                                                 | 786 us: 1.04x faster                                   |
| sqlglot_optimize        | 52.7 ms                                                | 50.8 ms: 1.04x faster                                  |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                   |
| coroutines              | 26.2 ms                                                | 25.2 ms: 1.04x faster                                  |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                   |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.03x faster                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 65.8 ms: 1.03x faster                                  |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                 |
| chaos                   | 68.7 ms                                                | 66.5 ms: 1.03x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 684 ms: 1.03x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                  |
| logging_simple          | 6.02 us                                                | 5.87 us: 1.03x faster                                  |
| coverage                | 99.3 ms                                                | 96.8 ms: 1.02x faster                                  |
| pickle_list             | 4.14 us                                                | 4.05 us: 1.02x faster                                  |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                   |
| regex_dna               | 203 ms                                                 | 199 ms: 1.02x faster                                   |
| tornado_http            | 96.5 ms                                                | 94.5 ms: 1.02x faster                                  |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.97 us: 1.01x faster                                  |
| dulwich_log             | 64.0 ms                                                | 63.1 ms: 1.01x faster                                  |
| telco                   | 6.43 ms                                                | 6.34 ms: 1.01x faster                                  |
| unpack_sequence         | 44.5 ns                                                | 43.9 ns: 1.01x faster                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                   |
| pickle_dict             | 31.2 us                                                | 30.8 us: 1.01x faster                                  |
| unpickle_list           | 4.99 us                                                | 4.95 us: 1.01x faster                                  |
| logging_format          | 6.48 us                                                | 6.43 us: 1.01x faster                                  |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| mako                    | 9.83 ms                                                | 9.95 ms: 1.01x slower                                  |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                   |
| xml_etree_process       | 53.7 ms                                                | 55.2 ms: 1.03x slower                                  |
| django_template         | 32.3 ms                                                | 33.3 ms: 1.03x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.56 ms: 1.03x slower                                  |
| chameleon               | 6.38 ms                                                | 6.58 ms: 1.03x slower                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                  |
| python_startup          | 8.58 ms                                                | 8.92 ms: 1.04x slower                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                  |
| nbody                   | 90.0 ms                                                | 94.8 ms: 1.05x slower                                  |
| generators              | 73.5 ms                                                | 77.5 ms: 1.05x slower                                  |
| xml_etree_generate      | 75.9 ms                                                | 80.5 ms: 1.06x slower                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.47 ms: 1.07x slower                                  |
| gc_traversal            | 3.82 ms                                                | 4.16 ms: 1.09x slower                                  |
| async_generators        | 356 ms                                                 | 428 ms: 1.20x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (11): djangocms, async_tree_none, async_tree_memoization, crypto_pyaes, sqlalchemy_imperative, bench_mp_pool, thrift, scimark_lu, meteor_contest, spectral_norm, unpickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
