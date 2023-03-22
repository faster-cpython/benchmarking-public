
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3eb12df
- commit date: 2023-02-11
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 181 ms: 1.12x slower                                   |
| chameleon      | 4.57 ms                                                | 4.34 ms: 1.05x faster                                  |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.00x faster                                 |
| tornado_http   | 72.4 ms                                                | 68.4 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 53.0 ms                                                | 49.7 ms: 1.07x faster                                  |
| nbody          | 65.5 ms                                                | 63.1 ms: 1.04x faster                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 71.0 ms: 1.08x faster                                  |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                  |
| regex_v8       | 16.2 ms                                                | 16.0 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.06 ms: 1.27x faster                                  |
| unpickle_pure_python | 159 us                                                 | 137 us: 1.16x faster                                   |
| xml_etree_parse      | 106 ms                                                 | 93.0 ms: 1.14x faster                                  |
| pickle_pure_python   | 199 us                                                 | 185 us: 1.08x faster                                   |
| xml_etree_iterparse  | 69.2 ms                                                | 67.1 ms: 1.03x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| xml_etree_generate   | 48.8 ms                                                | 49.2 ms: 1.01x slower                                  |
| unpickle_list        | 2.63 us                                                | 2.67 us: 1.02x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.02x slower                                  |
| unpickle             | 9.70 us                                                | 9.91 us: 1.02x slower                                  |
| pickle               | 7.17 us                                                | 7.57 us: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.38 ms: 1.26x faster                                  |
| python_startup         | 11.5 ms                                                | 9.36 ms: 1.23x faster                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.13 ms: 1.19x faster                                  |
| genshi_text     | 15.3 ms                                                | 13.8 ms: 1.11x faster                                  |
| genshi_xml      | 29.8 ms                                                | 27.5 ms: 1.08x faster                                  |
| django_template | 21.0 ms                                                | 20.8 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 411 ms: 1.58x faster                                   |
| pathlib                 | 27.8 ms                                                | 21.8 ms: 1.27x faster                                  |
| json_dumps              | 7.72 ms                                                | 6.06 ms: 1.27x faster                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.38 ms: 1.26x faster                                  |
| python_startup          | 11.5 ms                                                | 9.36 ms: 1.23x faster                                  |
| mako                    | 8.49 ms                                                | 7.13 ms: 1.19x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 137 us: 1.16x faster                                   |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.77 ms: 1.16x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 93.0 ms: 1.14x faster                                  |
| deltablue               | 2.81 ms                                                | 2.47 ms: 1.13x faster                                  |
| hexiom                  | 4.73 ms                                                | 4.21 ms: 1.12x faster                                  |
| genshi_text             | 15.3 ms                                                | 13.8 ms: 1.11x faster                                  |
| unpack_sequence         | 33.6 ns                                                | 30.6 ns: 1.10x faster                                  |
| richards                | 32.2 ms                                                | 29.5 ms: 1.09x faster                                  |
| chaos                   | 49.5 ms                                                | 45.5 ms: 1.09x faster                                  |
| genshi_xml              | 29.8 ms                                                | 27.5 ms: 1.08x faster                                  |
| regex_compile           | 76.7 ms                                                | 71.0 ms: 1.08x faster                                  |
| pickle_pure_python      | 199 us                                                 | 185 us: 1.08x faster                                   |
| float                   | 53.0 ms                                                | 49.7 ms: 1.07x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 24.7 us: 1.06x faster                                  |
| bench_thread_pool       | 473 us                                                 | 444 us: 1.06x faster                                   |
| logging_silent          | 68.0 ns                                                | 64.1 ns: 1.06x faster                                  |
| tornado_http            | 72.4 ms                                                | 68.4 ms: 1.06x faster                                  |
| create_gc_cycles        | 726 us                                                 | 687 us: 1.06x faster                                   |
| scimark_fft             | 199 ms                                                 | 189 ms: 1.05x faster                                   |
| chameleon               | 4.57 ms                                                | 4.34 ms: 1.05x faster                                  |
| dulwich_log             | 29.9 ms                                                | 28.4 ms: 1.05x faster                                  |
| sympy_str               | 152 ms                                                 | 144 ms: 1.05x faster                                   |
| pycparser               | 697 ms                                                 | 664 ms: 1.05x faster                                   |
| async_tree_memoization  | 336 ms                                                 | 320 ms: 1.05x faster                                   |
| sympy_sum               | 86.0 ms                                                | 82.1 ms: 1.05x faster                                  |
| deepcopy                | 224 us                                                 | 215 us: 1.04x faster                                   |
| fannkuch                | 261 ms                                                 | 251 ms: 1.04x faster                                   |
| nqueens                 | 61.8 ms                                                | 59.5 ms: 1.04x faster                                  |
| nbody                   | 65.5 ms                                                | 63.1 ms: 1.04x faster                                  |
| pprint_pformat          | 950 ms                                                 | 920 ms: 1.03x faster                                   |
| sympy_integrate         | 11.5 ms                                                | 11.1 ms: 1.03x faster                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 67.1 ms: 1.03x faster                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.86 us: 1.03x faster                                  |
| pprint_safe_repr        | 465 ms                                                 | 452 ms: 1.03x faster                                   |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.12 ms: 1.03x faster                                  |
| scimark_lu              | 72.1 ms                                                | 70.5 ms: 1.02x faster                                  |
| async_tree_none         | 285 ms                                                 | 278 ms: 1.02x faster                                   |
| sympy_expand            | 243 ms                                                 | 238 ms: 1.02x faster                                   |
| mdp                     | 1.54 sec                                               | 1.51 sec: 1.02x faster                                 |
| go                      | 109 ms                                                 | 107 ms: 1.02x faster                                   |
| meteor_contest          | 73.8 ms                                                | 72.7 ms: 1.02x faster                                  |
| regex_dna               | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| django_template         | 21.0 ms                                                | 20.8 ms: 1.01x faster                                  |
| gc_traversal            | 2.43 ms                                                | 2.41 ms: 1.01x faster                                  |
| sqlglot_normalize       | 171 ms                                                 | 169 ms: 1.01x faster                                   |
| regex_effbot            | 2.63 ms                                                | 2.60 ms: 1.01x faster                                  |
| regex_v8                | 16.2 ms                                                | 16.0 ms: 1.01x faster                                  |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.00x faster                                 |
| sqlglot_optimize        | 31.2 ms                                                | 31.1 ms: 1.00x faster                                  |
| logging_simple          | 3.50 us                                                | 3.51 us: 1.00x slower                                  |
| scimark_sor             | 83.0 ms                                                | 83.4 ms: 1.00x slower                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| logging_format          | 3.78 us                                                | 3.80 us: 1.01x slower                                  |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| spectral_norm           | 72.8 ms                                                | 73.4 ms: 1.01x slower                                  |
| xml_etree_generate      | 48.8 ms                                                | 49.2 ms: 1.01x slower                                  |
| unpickle_list           | 2.63 us                                                | 2.67 us: 1.02x slower                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.02x slower                                  |
| json                    | 2.77 ms                                                | 2.83 ms: 1.02x slower                                  |
| unpickle                | 9.70 us                                                | 9.91 us: 1.02x slower                                  |
| async_tree_io           | 706 ms                                                 | 726 ms: 1.03x slower                                   |
| coverage                | 58.6 ms                                                | 60.3 ms: 1.03x slower                                  |
| thrift                  | 433 us                                                 | 447 us: 1.03x slower                                   |
| crypto_pyaes            | 51.7 ms                                                | 53.4 ms: 1.03x slower                                  |
| coroutines              | 17.7 ms                                                | 18.4 ms: 1.04x slower                                  |
| pyflate                 | 311 ms                                                 | 324 ms: 1.04x slower                                   |
| raytrace                | 207 ms                                                 | 217 ms: 1.05x slower                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.18 ms: 1.05x slower                                  |
| sqlglot_parse           | 957 us                                                 | 1.01 ms: 1.05x slower                                  |
| pickle                  | 7.17 us                                                | 7.57 us: 1.06x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.37 us: 1.07x slower                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 50.0 ms: 1.08x slower                                  |
| 2to3                    | 161 ms                                                 | 181 ms: 1.12x slower                                   |
| generators              | 28.8 ms                                                | 32.9 ms: 1.14x slower                                  |
| async_generators        | 195 ms                                                 | 255 ms: 1.31x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (7): bench_mp_pool, telco, xml_etree_process, async_tree_cpu_io_mixed, sqlalchemy_declarative, html5lib, mypy2
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, comprehensions, dask, flaskblogging, gunicorn, pylint
