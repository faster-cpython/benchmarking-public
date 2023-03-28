
# Results vs. 3.10.4

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: darwin-arm64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 163 ms: 1.24x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.53 ms: 1.28x faster                                                 |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.22x faster                                                |
| html5lib       | 44.2 ms                                                | 35.0 ms: 1.26x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 63.9 ms: 1.46x faster                                                 |
| float          | 72.4 ms                                                | 52.0 ms: 1.39x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 74.5 ms: 1.29x faster                                                 |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                 |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 192 us: 1.47x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 143 us: 1.42x faster                                                  |
| json_dumps           | 8.40 ms                                                | 6.05 ms: 1.39x faster                                                 |
| xml_etree_process    | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| xml_etree_generate   | 54.2 ms                                                | 48.6 ms: 1.12x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 96.5 ms: 1.10x faster                                                 |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 69.4 ms: 1.04x faster                                                 |
| unpickle             | 9.89 us                                                | 9.76 us: 1.01x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| pickle_list          | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| pickle               | 7.35 us                                                | 7.44 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.3 ms: 1.03x slower                                                 |
| python_startup_no_site | 8.88 ms                                                | 10.2 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 37.2 ms                                                | 28.4 ms: 1.31x faster                                                 |
| mako            | 10.5 ms                                                | 8.12 ms: 1.29x faster                                                 |
| django_template | 27.3 ms                                                | 21.6 ms: 1.26x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.64 ms: 1.95x faster                                                 |
| logging_silent          | 119 ns                                                 | 66.4 ns: 1.80x faster                                                 |
| richards                | 51.4 ms                                                | 30.6 ms: 1.68x faster                                                 |
| scimark_sor             | 126 ms                                                 | 82.8 ms: 1.52x faster                                                 |
| go                      | 165 ms                                                 | 109 ms: 1.52x faster                                                  |
| scimark_lu              | 109 ms                                                 | 72.7 ms: 1.50x faster                                                 |
| raytrace                | 325 ms                                                 | 217 ms: 1.50x faster                                                  |
| asyncio_tcp             | 670 ms                                                 | 449 ms: 1.49x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 52.6 ms: 1.49x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 332 ms: 1.48x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 192 us: 1.47x faster                                                  |
| nbody                   | 93.3 ms                                                | 63.9 ms: 1.46x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 49.6 ms: 1.46x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 143 us: 1.42x faster                                                  |
| pyflate                 | 453 ms                                                 | 318 ms: 1.42x faster                                                  |
| float                   | 72.4 ms                                                | 52.0 ms: 1.39x faster                                                 |
| async_tree_none         | 400 ms                                                 | 288 ms: 1.39x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.05 ms: 1.39x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 748 ms: 1.36x faster                                                  |
| pycparser               | 916 ms                                                 | 676 ms: 1.35x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.44 us: 1.35x faster                                                 |
| logging_format          | 4.97 us                                                | 3.74 us: 1.33x faster                                                 |
| thrift                  | 580 us                                                 | 438 us: 1.32x faster                                                  |
| chaos                   | 66.7 ms                                                | 50.5 ms: 1.32x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.04 ms: 1.32x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 26.2 us: 1.31x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.20 ms: 1.31x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 462 ms: 1.31x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 939 ms: 1.31x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 28.4 ms: 1.31x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 73.4 ms: 1.31x faster                                                 |
| regex_compile           | 96.4 ms                                                | 74.5 ms: 1.29x faster                                                 |
| mako                    | 10.5 ms                                                | 8.12 ms: 1.29x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.94 ms: 1.28x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.53 ms: 1.28x faster                                                 |
| deepcopy                | 281 us                                                 | 221 us: 1.27x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 692 us: 1.27x faster                                                  |
| html5lib                | 44.2 ms                                                | 35.0 ms: 1.26x faster                                                 |
| django_template         | 27.3 ms                                                | 21.6 ms: 1.26x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 29.6 ms: 1.25x faster                                                 |
| fannkuch                | 317 ms                                                 | 254 ms: 1.25x faster                                                  |
| 2to3                    | 201 ms                                                 | 163 ms: 1.24x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.92 us: 1.23x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.81 ms: 1.23x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 546 ms: 1.23x faster                                                  |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.22x faster                                                |
| sqlglot_optimize        | 38.0 ms                                                | 31.3 ms: 1.21x faster                                                 |
| genshi_text             | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 462 us: 1.18x faster                                                  |
| scimark_fft             | 230 ms                                                 | 195 ms: 1.18x faster                                                  |
| dask                    | 265 ms                                                 | 226 ms: 1.18x faster                                                  |
| async_generators        | 234 ms                                                 | 200 ms: 1.17x faster                                                  |
| sympy_integrate         | 13.3 ms                                                | 11.4 ms: 1.16x faster                                                 |
| mypy2                   | 307 ms                                                 | 263 ms: 1.16x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 32.7 ns: 1.15x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 172 ms: 1.14x faster                                                  |
| sympy_expand            | 275 ms                                                 | 242 ms: 1.14x faster                                                  |
| nqueens                 | 68.2 ms                                                | 60.5 ms: 1.13x faster                                                 |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 48.6 ms: 1.12x faster                                                 |
| json                    | 3.08 ms                                                | 2.78 ms: 1.11x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 96.5 ms: 1.10x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.35 us: 1.09x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 85.9 ms: 1.09x faster                                                 |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.7 ms: 1.08x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                                |
| telco                   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                 |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 69.4 ms: 1.04x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 75.1 ms: 1.04x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                 |
| unpickle                | 9.89 us                                                | 9.76 us: 1.01x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| comprehensions          | 17.6 us                                                | 17.7 us: 1.00x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| pickle                  | 7.35 us                                                | 7.44 us: 1.01x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.3 ms: 1.03x slower                                                 |
| generators              | 32.7 ms                                                | 33.7 ms: 1.03x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                 |
| gc_traversal            | 2.39 ms                                                | 2.56 ms: 1.07x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 44.0 ms: 1.11x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 10.2 ms: 1.15x slower                                                 |
| coverage                | 42.0 ms                                                | 57.2 ms: 1.36x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
