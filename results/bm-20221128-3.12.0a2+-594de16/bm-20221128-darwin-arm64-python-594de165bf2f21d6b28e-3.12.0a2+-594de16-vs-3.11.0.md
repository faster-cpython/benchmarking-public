
# Results vs. 3.11.0

- fork: python
- ref: 594de165bf2f21d6b28e
- machine: darwin-arm64
- commit hash: 594de16
- commit date: 2022-11-28
- overall geometric mean: 1.02x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 186 ms: 1.15x slower                                                   |
| chameleon      | 4.57 ms                                                | 4.64 ms: 1.01x slower                                                  |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                 |
| html5lib       | 34.7 ms                                                | 36.1 ms: 1.04x slower                                                  |
| tornado_http   | 72.4 ms                                                | 68.3 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 65.0 ms: 1.01x faster                                                  |
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                                   |
| float          | 53.0 ms                                                | 56.4 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_compile  | 76.7 ms                                                | 75.9 ms: 1.01x faster                                                  |
| regex_v8       | 16.2 ms                                                | 16.0 ms: 1.01x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.07 ms: 1.27x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 93.2 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 66.4 ms: 1.04x faster                                                  |
| unpickle_list        | 2.63 us                                                | 2.59 us: 1.02x faster                                                  |
| xml_etree_generate   | 48.8 ms                                                | 48.7 ms: 1.00x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                  |
| unpickle_pure_python | 159 us                                                 | 161 us: 1.01x slower                                                   |
| pickle_list          | 2.81 us                                                | 2.85 us: 1.01x slower                                                  |
| unpickle             | 9.70 us                                                | 9.84 us: 1.01x slower                                                  |
| json_loads           | 16.1 us                                                | 16.4 us: 1.02x slower                                                  |
| pickle               | 7.17 us                                                | 7.54 us: 1.05x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 210 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.33 ms: 1.27x faster                                                  |
| python_startup         | 11.5 ms                                                | 9.29 ms: 1.24x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.24 ms: 1.03x faster                                                  |
| genshi_xml      | 29.8 ms                                                | 29.6 ms: 1.01x faster                                                  |
| genshi_text     | 15.3 ms                                                | 15.2 ms: 1.00x faster                                                  |
| django_template | 21.0 ms                                                | 21.6 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.6 ms: 1.35x faster                                                  |
| json_dumps              | 7.72 ms                                                | 6.07 ms: 1.27x faster                                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.33 ms: 1.27x faster                                                  |
| python_startup          | 11.5 ms                                                | 9.29 ms: 1.24x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 93.2 ms: 1.14x faster                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.83 ms: 1.13x faster                                                  |
| tornado_http            | 72.4 ms                                                | 68.3 ms: 1.06x faster                                                  |
| logging_silent          | 68.0 ns                                                | 64.4 ns: 1.06x faster                                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 66.4 ms: 1.04x faster                                                  |
| async_tree_memoization  | 336 ms                                                 | 323 ms: 1.04x faster                                                   |
| bench_thread_pool       | 473 us                                                 | 456 us: 1.04x faster                                                   |
| mako                    | 8.49 ms                                                | 8.24 ms: 1.03x faster                                                  |
| richards                | 32.2 ms                                                | 31.3 ms: 1.03x faster                                                  |
| bench_mp_pool           | 43.2 ms                                                | 42.1 ms: 1.03x faster                                                  |
| dulwich_log             | 29.9 ms                                                | 29.3 ms: 1.02x faster                                                  |
| unpickle_list           | 2.63 us                                                | 2.59 us: 1.02x faster                                                  |
| scimark_lu              | 72.1 ms                                                | 71.0 ms: 1.02x faster                                                  |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_compile           | 76.7 ms                                                | 75.9 ms: 1.01x faster                                                  |
| regex_v8                | 16.2 ms                                                | 16.0 ms: 1.01x faster                                                  |
| regex_effbot            | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                  |
| genshi_xml              | 29.8 ms                                                | 29.6 ms: 1.01x faster                                                  |
| nbody                   | 65.5 ms                                                | 65.0 ms: 1.01x faster                                                  |
| coverage                | 58.6 ms                                                | 58.2 ms: 1.01x faster                                                  |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                 |
| scimark_fft             | 199 ms                                                 | 198 ms: 1.00x faster                                                   |
| genshi_text             | 15.3 ms                                                | 15.2 ms: 1.00x faster                                                  |
| xml_etree_generate      | 48.8 ms                                                | 48.7 ms: 1.00x faster                                                  |
| mdp                     | 1.54 sec                                               | 1.54 sec: 1.00x faster                                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                  |
| sympy_sum               | 86.0 ms                                                | 86.6 ms: 1.01x slower                                                  |
| pidigits                | 281 ms                                                 | 283 ms: 1.01x slower                                                   |
| telco                   | 3.39 ms                                                | 3.43 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 539 ms: 1.01x slower                                                   |
| sqlglot_normalize       | 171 ms                                                 | 173 ms: 1.01x slower                                                   |
| thrift                  | 433 us                                                 | 438 us: 1.01x slower                                                   |
| unpickle_pure_python    | 159 us                                                 | 161 us: 1.01x slower                                                   |
| spectral_norm           | 72.8 ms                                                | 73.7 ms: 1.01x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 31.6 ms: 1.01x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.01x slower                                                  |
| unpickle                | 9.70 us                                                | 9.84 us: 1.01x slower                                                  |
| chameleon               | 4.57 ms                                                | 4.64 ms: 1.01x slower                                                  |
| sympy_expand            | 243 ms                                                 | 247 ms: 1.02x slower                                                   |
| json_loads              | 16.1 us                                                | 16.4 us: 1.02x slower                                                  |
| sympy_str               | 152 ms                                                 | 155 ms: 1.02x slower                                                   |
| sympy_integrate         | 11.5 ms                                                | 11.8 ms: 1.03x slower                                                  |
| django_template         | 21.0 ms                                                | 21.6 ms: 1.03x slower                                                  |
| json                    | 2.77 ms                                                | 2.86 ms: 1.03x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.4 ms: 1.03x slower                                                  |
| chaos                   | 49.5 ms                                                | 51.1 ms: 1.03x slower                                                  |
| logging_format          | 3.78 us                                                | 3.91 us: 1.03x slower                                                  |
| logging_simple          | 3.50 us                                                | 3.62 us: 1.03x slower                                                  |
| async_tree_io           | 706 ms                                                 | 733 ms: 1.04x slower                                                   |
| html5lib                | 34.7 ms                                                | 36.1 ms: 1.04x slower                                                  |
| sqlglot_parse           | 957 us                                                 | 996 us: 1.04x slower                                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.17 ms: 1.04x slower                                                  |
| hexiom                  | 4.73 ms                                                | 4.93 ms: 1.04x slower                                                  |
| meteor_contest          | 73.8 ms                                                | 77.2 ms: 1.05x slower                                                  |
| async_generators        | 195 ms                                                 | 204 ms: 1.05x slower                                                   |
| pickle                  | 7.17 us                                                | 7.54 us: 1.05x slower                                                  |
| pprint_safe_repr        | 465 ms                                                 | 491 ms: 1.06x slower                                                   |
| fannkuch                | 261 ms                                                 | 276 ms: 1.06x slower                                                   |
| pickle_pure_python      | 199 us                                                 | 210 us: 1.06x slower                                                   |
| pprint_pformat          | 950 ms                                                 | 1.00 sec: 1.06x slower                                                 |
| raytrace                | 207 ms                                                 | 220 ms: 1.06x slower                                                   |
| float                   | 53.0 ms                                                | 56.4 ms: 1.06x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.04 us: 1.07x slower                                                  |
| deepcopy                | 224 us                                                 | 240 us: 1.07x slower                                                   |
| go                      | 109 ms                                                 | 118 ms: 1.09x slower                                                   |
| deepcopy_memo           | 26.3 us                                                | 29.5 us: 1.12x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.43 us: 1.13x slower                                                  |
| coroutines              | 17.7 ms                                                | 20.0 ms: 1.13x slower                                                  |
| pyflate                 | 311 ms                                                 | 356 ms: 1.14x slower                                                   |
| 2to3                    | 161 ms                                                 | 186 ms: 1.15x slower                                                   |
| generators              | 28.8 ms                                                | 34.1 ms: 1.19x slower                                                  |
| scimark_sor             | 83.0 ms                                                | 99.3 ms: 1.20x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 56.3 ms: 1.21x slower                                                  |
| unpack_sequence         | 33.6 ns                                                | 62.7 ns: 1.87x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (5): xml_etree_process, deltablue, nqueens, async_tree_none, pycparser
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221128-3.12.0a2+-594de16/bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16.json: mypy
