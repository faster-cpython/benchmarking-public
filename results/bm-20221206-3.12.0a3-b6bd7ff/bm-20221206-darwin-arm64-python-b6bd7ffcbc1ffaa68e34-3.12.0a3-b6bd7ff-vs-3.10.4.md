
# Results vs. 3.10.4

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: darwin-arm64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.10x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 178 ms: 1.13x faster                                                  |
| chameleon      | 5.79 ms                                                | 5.09 ms: 1.14x faster                                                 |
| docutils       | 1.78 sec                                               | 1.53 sec: 1.16x faster                                                |
| html5lib       | 44.2 ms                                                | 38.5 ms: 1.15x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.2 ms: 1.43x faster                                                 |
| float          | 72.4 ms                                                | 59.1 ms: 1.23x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 83.2 ms: 1.16x faster                                                 |
| regex_v8       | 17.6 ms                                                | 15.8 ms: 1.11x faster                                                 |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.40 ms                                                | 6.32 ms: 1.33x faster                                                 |
| pickle_pure_python   | 283 us                                                 | 229 us: 1.24x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 177 us: 1.15x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 40.4 ms: 1.11x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 97.6 ms: 1.09x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.57 us: 1.05x faster                                                 |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                                 |
| unpickle             | 9.89 us                                                | 9.61 us: 1.03x faster                                                 |
| xml_etree_generate   | 54.2 ms                                                | 53.8 ms: 1.01x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 74.3 ms: 1.03x slower                                                 |
| pickle               | 7.35 us                                                | 7.61 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.3 ms: 1.03x slower                                                 |
| python_startup_no_site | 8.88 ms                                                | 10.2 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.37 ms: 1.42x faster                                                 |
| django_template | 27.3 ms                                                | 24.6 ms: 1.11x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 34.6 ms: 1.07x faster                                                 |
| genshi_text     | 18.4 ms                                                | 17.5 ms: 1.05x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 3.06 ms: 1.68x faster                                                 |
| nbody                   | 93.3 ms                                                | 65.2 ms: 1.43x faster                                                 |
| raytrace                | 325 ms                                                 | 228 ms: 1.42x faster                                                  |
| mako                    | 10.5 ms                                                | 7.37 ms: 1.42x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 55.1 ms: 1.42x faster                                                 |
| richards                | 51.4 ms                                                | 37.0 ms: 1.39x faster                                                 |
| logging_silent          | 119 ns                                                 | 86.1 ns: 1.39x faster                                                 |
| json_dumps              | 8.40 ms                                                | 6.32 ms: 1.33x faster                                                 |
| go                      | 165 ms                                                 | 125 ms: 1.33x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 792 ms: 1.29x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 384 ms: 1.28x faster                                                  |
| async_tree_none         | 400 ms                                                 | 316 ms: 1.27x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 695 us: 1.27x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.09 ms: 1.26x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 57.9 ms: 1.25x faster                                                 |
| chaos                   | 66.7 ms                                                | 53.3 ms: 1.25x faster                                                 |
| pycparser               | 916 ms                                                 | 734 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.78 ms: 1.24x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.27 ms: 1.24x faster                                                 |
| pyflate                 | 453 ms                                                 | 366 ms: 1.24x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 229 us: 1.24x faster                                                  |
| scimark_lu              | 109 ms                                                 | 88.5 ms: 1.24x faster                                                 |
| float                   | 72.4 ms                                                | 59.1 ms: 1.23x faster                                                 |
| thrift                  | 580 us                                                 | 478 us: 1.22x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 573 ms: 1.17x faster                                                  |
| scimark_fft             | 230 ms                                                 | 198 ms: 1.16x faster                                                  |
| fannkuch                | 317 ms                                                 | 273 ms: 1.16x faster                                                  |
| scimark_sor             | 126 ms                                                 | 109 ms: 1.16x faster                                                  |
| docutils                | 1.78 sec                                               | 1.53 sec: 1.16x faster                                                |
| regex_compile           | 96.4 ms                                                | 83.2 ms: 1.16x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 32.0 ms: 1.16x faster                                                 |
| html5lib                | 44.2 ms                                                | 38.5 ms: 1.15x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 177 us: 1.15x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 531 ms: 1.14x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 84.2 ms: 1.14x faster                                                 |
| chameleon               | 5.79 ms                                                | 5.09 ms: 1.14x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 1.08 sec: 1.14x faster                                                |
| 2to3                    | 201 ms                                                 | 178 ms: 1.13x faster                                                  |
| hexiom                  | 6.32 ms                                                | 5.60 ms: 1.13x faster                                                 |
| logging_format          | 4.97 us                                                | 4.46 us: 1.12x faster                                                 |
| logging_simple          | 4.63 us                                                | 4.16 us: 1.11x faster                                                 |
| dask                    | 265 ms                                                 | 238 ms: 1.11x faster                                                  |
| regex_v8                | 17.6 ms                                                | 15.8 ms: 1.11x faster                                                 |
| django_template         | 27.3 ms                                                | 24.6 ms: 1.11x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 40.4 ms: 1.11x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 97.6 ms: 1.09x faster                                                 |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| telco                   | 3.63 ms                                                | 3.37 ms: 1.08x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 34.6 ms: 1.07x faster                                                 |
| json                    | 3.08 ms                                                | 2.88 ms: 1.07x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 35.8 ms: 1.06x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 516 us: 1.06x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 32.6 us: 1.06x faster                                                 |
| genshi_text             | 18.4 ms                                                | 17.5 ms: 1.05x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.57 us: 1.05x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 12.8 ms: 1.04x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.42 us: 1.04x faster                                                 |
| deepcopy                | 281 us                                                 | 272 us: 1.03x faster                                                  |
| json_loads              | 16.9 us                                                | 16.4 us: 1.03x faster                                                 |
| unpickle                | 9.89 us                                                | 9.61 us: 1.03x faster                                                 |
| asyncio_tcp             | 670 ms                                                 | 651 ms: 1.03x faster                                                  |
| pathlib                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 2.32 us: 1.02x faster                                                 |
| sympy_expand            | 275 ms                                                 | 270 ms: 1.02x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 92.1 ms: 1.02x faster                                                 |
| sympy_str               | 169 ms                                                 | 168 ms: 1.01x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 53.8 ms: 1.01x faster                                                 |
| async_generators        | 234 ms                                                 | 233 ms: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.67 sec: 1.01x slower                                                |
| sqlglot_normalize       | 196 ms                                                 | 197 ms: 1.01x slower                                                  |
| pickle_list             | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                                 |
| meteor_contest          | 78.1 ms                                                | 79.4 ms: 1.02x slower                                                 |
| nqueens                 | 68.2 ms                                                | 70.0 ms: 1.03x slower                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 74.3 ms: 1.03x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.3 ms: 1.03x slower                                                 |
| pickle                  | 7.35 us                                                | 7.61 us: 1.03x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                 |
| comprehensions          | 17.6 us                                                | 19.0 us: 1.08x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 44.8 ms: 1.13x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 10.2 ms: 1.15x slower                                                 |
| coroutines              | 20.2 ms                                                | 24.5 ms: 1.22x slower                                                 |
| generators              | 32.7 ms                                                | 42.2 ms: 1.29x slower                                                 |
| unpack_sequence         | 37.4 ns                                                | 52.7 ns: 1.41x slower                                                 |
| coverage                | 42.0 ms                                                | 64.8 ms: 1.54x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (2): mypy2, pickle_dict
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
